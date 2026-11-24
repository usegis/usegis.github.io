// Builds the site into _site/: the static files as they are, and each pages/*.md through pages/template.html.
import { cpSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync } from "node:fs";
import MarkdownIt from "markdown-it";

const OUT = "_site";
const SKIP = new Set([".git", ".github", ".gitignore", ".DS_Store", "node_modules", "package.json", "package-lock.json",
  "CLAUDE.md", "docs", "bin", "pages", OUT]);
const md = new MarkdownIt({ html: false, typographer: false });
const template = readFileSync("pages/template.html", "utf8");

const slug = (text) => text.toLowerCase().replace(/&[a-z]+;/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

// "## 1. Live layer" becomes a numbered level with the anchor #live-layer; other headings are notes.
function sections(html) {
  return html.split(/(?=<h2>)/).map((chunk) => {
    const level = chunk.match(/^<h2>(\d+)\. (.+?)<\/h2>\n?/);
    if (level) {
      const body = chunk.slice(level[0].length).trimEnd();
      return `<section class="level" id="${slug(level[2])}">\n<h2><span>${level[1]}</span> ${level[2]}</h2>\n${body}\n</section>\n`;
    }
    return chunk.replace(/^<h2>/, '<h2 class="note">');
  }).join("");
}

function page(markdown) {
  const title = markdown.match(/^# (.+)$/m)[1];
  const html = sections(md.render(markdown))
    .replace(/<p>Who: /g, '<p class="who">')
    .replace(/<p>See also: /g, '<p class="next">See also: ');
  return template.replace("{{title}}", title).replace("{{content}}", html.trimEnd());
}

rmSync(OUT, { recursive: true, force: true });
mkdirSync(OUT);
for (const name of readdirSync(".")) {
  if (!SKIP.has(name)) cpSync(name, `${OUT}/${name}`, { recursive: true });
}
for (const name of readdirSync("pages").filter((n) => n.endsWith(".md"))) {
  writeFileSync(`${OUT}/${name.replace(/\.md$/, ".html")}`, page(readFileSync(`pages/${name}`, "utf8")));
}
console.log(`built ${OUT}/`);
