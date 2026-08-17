/* Fleet net P&L box — guards the headline number on docs/fleet.html.
 *
 * Why this exists: the box sums a HARDCODED list of books. hypecrypto
 * launched 2026-08-15 and was left out for two days, so the fleet total
 * silently understated the money. This test extracts the REAL script out
 * of fleet.html, runs it against the real published JSONs with a recording
 * canvas/fetch shim, and fails if any published paper book is missing.
 *
 * Run directly:  node tests/test_fleet_net.js
 */
const fs = require("fs");
const path = require("path");
const assert = require("assert");

const ROOT = path.resolve(__dirname, "..");
const DOCS = path.join(ROOT, "docs");
const html = fs.readFileSync(path.join(DOCS, "fleet.html"), "utf8");

const m = html.match(/\/\* Fleet net P&L[\s\S]*?\n\}\)\(\);/);
assert(m, "netbox script block not found in fleet.html");
const block = m[0];

// --- the list itself -------------------------------------------------
assert(!/"stock"/.test(block), "retired stock book must not be in ACTIVE");
assert(!/"lottery"/.test(block),
  "lottery is REAL money on another scale — never mix it into the paper total");
for (const f of fs.readdirSync(DOCS)) {
  const mm = f.match(/^(.+)_dashboard_data\.json$/);
  if (!mm || mm[1] === "stock") continue;          // stock = frozen archive
  assert(block.includes(`"${mm[1]}"`),
    `published book ${mm[1]} is missing from ACTIVE — its money vanishes ` +
    `from the fleet total (add it to the list in docs/fleet.html)`);
}

// --- the rendered box ------------------------------------------------
const els = { netv: {}, netsub: {} };
global.document = { getElementById: id => els[id] };
global.fetch = async name => {
  const p = path.join(DOCS, name);
  if (!fs.existsSync(p)) return { ok: false };
  return { ok: true, json: async () => JSON.parse(fs.readFileSync(p, "utf8")) };
};
global.setInterval = () => {};
eval(block);

setTimeout(() => {
  const names = [...block.matchAll(/"([a-z]+)"/g)].map(x => x[1])
    .filter(n => fs.existsSync(path.join(DOCS, n + "_dashboard_data.json")));
  let staked = 0, value = 0;
  for (const n of names) {
    const d = JSON.parse(fs.readFileSync(
      path.join(DOCS, n + "_dashboard_data.json"), "utf8"));
    const live = d.intraday && d.intraday.length
      ? d.intraday[d.intraday.length - 1] : d.current;
    staked += d.starting_cash;
    value += live.value;
  }
  const net = value - staked;
  const pct = (net / staked * 100).toFixed(2);
  const dollars = Math.abs(net).toLocaleString("en-US",
    { minimumFractionDigits: 2, maximumFractionDigits: 2 });

  assert(els.netv.textContent.includes(dollars),
    `expected $${dollars} in "${els.netv.textContent}"`);
  assert(els.netv.textContent.includes(pct + "%"),
    `expected ${pct}% in "${els.netv.textContent}"`);
  assert.strictEqual(els.netv.className, "v " + (net >= 0 ? "up" : "down"));
  assert(els.netsub.textContent.includes(`${names.length} active books`),
    `book count wrong: "${els.netsub.textContent}"`);
  assert(!/NaN|undefined/.test(els.netv.textContent + els.netsub.textContent),
    "NaN/undefined leaked into the box");

  console.log("netv :", els.netv.textContent);
  console.log("sub  :", els.netsub.textContent);
  console.log(`\nOK — ${names.length} books, box matches independent recompute`);
}, 400);
