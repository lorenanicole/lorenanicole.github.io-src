Title: The Refit: What Python 3.15 Actually Looks Like When You Ship It
Date: 2026-10-09
Author: Lorena Mesa
Category: Python
Tags: Python, Python 3.15, AI, LLMs, Agentic Coding, PydanticAI, uv, FastAPI, RAG, PostgreSQL, Railway, Playwright, Chicago, Star Trek
Slug: the-refit-python-315
Summary: Python 3.15 final shipped today. Here's what it actually looks like in production — lazy imports, frozendict, sentinel, a stdlib sampling profiler, and a 7-12% JIT — in EventLoop, a Chicago events chatbot on Python 3.15, uv, FastAPI and PydanticAI.

I have a confession. When the Star Trek reboot dropped in 2009 and everyone started using "warp speed" as a metaphor for tech velocity, I rolled my eyes — not because I'm not a fan, but because I *am*. I grew up on TNG (Star Trek: The Next Generation — Picard's Enterprise, the holodeck, the best theme music in television history). I'm working through Klingon with the [Klingon Language Institute](https://www.kli.org/members-only/klcp-prep/), I have the Vulcan salute in muscle memory, and I own three Maine Coons including Purrcard my tuxedo boy, which I think qualifies me as a Data apologist. So when I say Python 3.15 feels like a freshly refit Enterprise — more capable, leaner, the crew the same but the ship better — I mean it with full nerd sincerity.

In my [last post]({filename}why-im-blogging-again.md), I wrote about how AI has collapsed the old divisions in software engineering. This post gets specific. I've been building **EventLoop** — a Chicago events discovery chatbot, now live at **[eventloop.city](https://eventloop.city)**. A Python backend that scrapes venue calendars, talks to Claude via PydanticAI, and serves a streaming SSE chat API to a TypeScript frontend. I built it on the Python 3.15 release candidates; final dropped the morning this went up. Here's what that looks like, where 3.15 shines, and why — if you're building AI pipelines in 2026 — it's the version to be on.

<div id="lcars-panel" style="margin:2.5rem auto;max-width:620px;font-family:monospace;"><noscript><img src="/images/refit-python-315-card.svg" alt="EventLoop LCARS mission brief — STARDATE 2026.282, Python 3.15, FastAPI, PydanticAI, 569 tests, Railway" style="width:100%;border-radius:4px;"></noscript></div>
<script>
(function(){
  var el=document.getElementById('lcars-panel');
  var AMBER='#FF9900',BLUE='#9999FF',RED='#CC4444',WHITE='#F1F5F9',DIM='#475569',BG='#0a0a0f';
  var W=620,H=340;
  var svg='<svg viewBox="0 0 '+W+' '+H+'" xmlns="http://www.w3.org/2000/svg" style="width:100%;display:block;border-radius:4px;">';
  svg+='<rect width="'+W+'" height="'+H+'" fill="'+BG+'"/>';
  // Left LCARS elbow
  svg+='<rect x="0" y="0" width="72" height="72" rx="36" fill="'+AMBER+'"/>';
  svg+='<rect x="36" y="0" width="36" height="72" fill="'+AMBER+'"/>';
  svg+='<rect x="0" y="36" width="72" height="36" fill="'+AMBER+'"/>';
  svg+='<rect x="8" y="8" width="60" height="60" rx="28" fill="'+BG+'"/>';
  svg+='<rect x="36" y="8" width="36" height="60" fill="'+BG+'"/>';
  svg+='<rect x="8" y="36" width="60" height="36" fill="'+BG+'"/>';
  svg+='<rect x="0" y="72" width="20" height="'+(H-92)+'" fill="'+AMBER+'"/>';
  svg+='<rect x="0" y="'+(H-56)+'" width="72" height="20" fill="'+BLUE+'"/>';
  svg+='<rect x="0" y="'+(H-32)+'" width="72" height="14" fill="'+RED+'"/>';
  svg+='<rect x="0" y="'+(H-14)+'" width="72" height="14" fill="'+AMBER+'"/>';
  // Right spine
  svg+='<rect x="'+(W-20)+'" y="72" width="20" height="'+(H-92)+'" fill="'+BLUE+'"/>';
  svg+='<rect x="'+(W-72)+'" y="'+(H-20)+'" width="72" height="20" fill="'+BLUE+'"/>';
  svg+='<rect x="'+(W-72)+'" y="0" width="20" height="72" fill="'+AMBER+'"/>';
  svg+='<rect x="'+(W-72)+'" y="0" width="72" height="20" fill="'+AMBER+'"/>';
  // Top title bar
  svg+='<rect x="80" y="0" width="'+(W-160)+'" height="20" fill="'+AMBER+'"/>';
  svg+='<rect x="80" y="24" width="'+(W-160)+'" height="10" fill="'+BLUE+'" opacity="0.7"/>';
  svg+='<text x="'+W/2+'" y="15" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="'+BG+'" letter-spacing="2">STARFLEET MISSION BRIEF — SECTOR CHICAGO-ILL</text>';
  // Content area
  var CX=88,CY=44,CW=W-176;
  svg+='<text x="'+CX+'" y="'+(CY+14)+'" font-family="monospace" font-size="9" fill="'+AMBER+'" letter-spacing="2">STARDATE 2026.282</text>';
  svg+='<text x="'+(CX+CW)+'" y="'+(CY+14)+'" text-anchor="end" font-family="monospace" font-size="9" fill="'+BLUE+'" letter-spacing="2">CLASSIFICATION: OPEN SOURCE</text>';
  // Chicago flag
  var FX=CX,FY=CY+24,FW=196,FH=104;
  svg+='<rect x="'+FX+'" y="'+FY+'" width="'+FW+'" height="'+FH+'" fill="#F0F0F0" rx="2"/>';
  var s1y=FY+Math.round(FH*0.29),s2y=FY+Math.round(FH*0.59),sh=Math.round(FH*0.14);
  svg+='<rect x="'+FX+'" y="'+s1y+'" width="'+FW+'" height="'+sh+'" fill="#4169A4"/>';
  svg+='<rect x="'+FX+'" y="'+s2y+'" width="'+FW+'" height="'+sh+'" fill="#4169A4"/>';
  var starCY=FY+FH/2,starR=10;
  [0.2,0.4,0.6,0.8].forEach(function(f){
    var sx=FX+FW*f,pts='';
    for(var i=0;i<12;i++){var r=i%2===0?starR:starR*0.45,a=(i*30-90)*Math.PI/180;pts+=(sx+r*Math.cos(a)).toFixed(1)+','+(starCY+r*Math.sin(a)).toFixed(1)+' ';}
    svg+='<polygon points="'+pts.trim()+'" fill="#CC2A27"/>';
  });
  svg+='<rect x="'+FX+'" y="'+FY+'" width="'+FW+'" height="'+FH+'" fill="none" stroke="'+DIM+'" stroke-width="1" rx="2"/>';
  svg+='<text x="'+(FX+FW/2)+'" y="'+(FY+FH+13)+'" text-anchor="middle" font-family="monospace" font-size="8" fill="'+DIM+'">CITY OF CHICAGO · EST. 1837</text>';
  // Stats
  var SX=CX+FW+16,SY=FY,SW=CW-FW-16;
  var stats=[
    ['DESIGNATION','EVENTLOOP'],['REGISTRY','PY-3.15 / UV-0.12.24'],
    ['PROPULSION','ASYNCPG + FASTAPI SSE'],['INTELLIGENCE','CLAUDE SONNET 5.5'],
    ['DATABASE','CHICAGO EVENTS · GROWING DAILY'],['SECTORS','90 NEIGHBORHOODS'],
    ['CREW','569 TESTS · 0 RUFF ERRORS'],['DEPLOYMENT','RAILWAY · ~$12/MO'],
  ];
  stats.forEach(function(s,i){
    var sy=SY+i*16;
    svg+='<text x="'+SX+'" y="'+(sy+11)+'" font-family="monospace" font-size="8" fill="'+AMBER+'" letter-spacing="1">'+s[0]+'</text>';
    svg+='<text x="'+(SX+SW)+'" y="'+(sy+11)+'" text-anchor="end" font-family="monospace" font-size="8" fill="'+WHITE+'">'+s[1]+'</text>';
    svg+='<line x1="'+SX+'" y1="'+(sy+14)+'" x2="'+(SX+SW)+'" y2="'+(sy+14)+'" stroke="'+DIM+'" stroke-width="0.5" opacity="0.4"/>';
  });
  // Status bar
  var scanY=CY+24+FH+20;
  svg+='<line x1="'+CX+'" y1="'+scanY+'" x2="'+(CX+CW)+'" y2="'+scanY+'" stroke="'+DIM+'" stroke-width="0.5" opacity="0.4"/>';
  svg+='<text x="'+CX+'" y="'+(scanY+14)+'" font-family="monospace" font-size="8" fill="'+AMBER+'" letter-spacing="1">MISSION STATUS</text>';
  svg+='<text x="'+(CX+CW)+'" y="'+(scanY+14)+'" text-anchor="end" font-family="monospace" font-size="8" fill="#44CC44">● OPERATIONAL</text>';
  var blurbs=['▸ SCRAPER ARRAY ONLINE — NEXT SWEEP IN APPROX 6 HOURS','▸ INTENT CLASSIFIER STANDING BY — HAIKU CLASS, LOW ENERGY','▸ SEMANTIC INDEX LOADED — MODEL2VEC · 0.3ms QUERY TIME'];
  blurbs.forEach(function(b,i){svg+='<text x="'+CX+'" y="'+(scanY+28+i*13)+'" font-family="monospace" font-size="7.5" fill="'+DIM+'">'+b+'</text>';});
  svg+='<style>@keyframes lcblink{0%,100%{opacity:1}50%{opacity:0}}.lcb{animation:lcblink 1.2s step-start infinite}</style>';
  svg+='<text class="lcb" x="'+CX+'" y="'+(scanY+67)+'" font-family="monospace" font-size="9" fill="'+AMBER+'">█</text>';
  svg+='</svg>';
  el.innerHTML=svg;
  el.style.opacity='0';el.style.transition='opacity 0.7s ease';
  if('IntersectionObserver' in window){new IntersectionObserver(function(e,o){if(e[0].isIntersecting){el.style.opacity='1';o.disconnect();}},{threshold:0.2}).observe(el);}
  else{el.style.opacity='1';}
})();
</script>

## What Is EventLoop?

EventLoop answers questions like *"what's happening in Logan Square this weekend?"* with real answers — pulled from a **PostgreSQL** database of scraped Chicago venue events, optionally enriched by a live Google Events fallback via SerpAPI (which times out on roughly a third of calls at 90s — the local database answers first, so a dropped web search degrades rather than breaks the response). The chatbot uses Claude Sonnet 5.5 via PydanticAI, a Claude Haiku 4.5-powered intent classifier to gate the expensive agent, and a semantic embedding index (model2vec — no torch dependency, queries in ~0.3ms) for fast local retrieval.

**Three services on Railway, one PostgreSQL database:**

- **`api`** — Python 3.15, FastAPI with Server-Sent Events, always-on
- **`frontend`** — nginx serving a TypeScript/Vite UI, proxying `/api/*` to the backend at runtime
- **`scraper`** — Python 3.15, Playwright 1.63 + BeautifulSoup4, cron every six hours

The stack:

- **Python 3.15** — API, scraper, all of it
- **uv 0.12.24** for environment and dependency management
- **FastAPI** + Server-Sent Events for streaming chat
- **PydanticAI** for the agent layer
- **Anthropic** (Claude Sonnet 5.5 for chat, Claude Haiku 4.5 for intent classification)
- **SQLAlchemy async** + asyncpg for PostgreSQL
- **Playwright** + BeautifulSoup4 for scrapers that need JavaScript rendering
- **model2vec** for semantic search (no torch, no CUDA, no drama)
- **ruff** for linting — zero errors, every suppression documented
- **Railway** for deployment — three services, one PostgreSQL database, ~$10–12/month

## uv: The Transporter Beam for Python Environments

Before the language features: **uv**, now at version **0.12.24**, has listed Python 3.15 as supported since [#18552](https://github.com/astral-sh/uv/pull/18552) (merged March 18, 2026) — tracking every alpha, beta, and release candidate long before final dropped.

The pitch used to be "pip but fast." That undersells what it is now. uv is your Python installer, virtual environment manager, lockfile manager, script runner, and workspace tool in one binary with no system Python requirement. For EventLoop I have a single `pyproject.toml` with optional dependency groups:

```toml
[project]
requires-python = ">=3.15"

[project.optional-dependencies]
app = [
    "fastapi>=0.115.0",
    "pydantic-ai>=2.50.0",
    "anthropic>=0.45.0",
    "sqlalchemy[asyncio]>=2.0.0",
    "asyncpg>=0.32.0",
    ...
]
parser = [
    "playwright>=1.63.0",
    "beautifulsoup4>=4.12.0",
    "sqlalchemy[asyncio]>=2.0.0",
    "asyncpg>=0.32.0",
    ...
]
test = ["pytest>=7.4.0", "pytest-asyncio>=0.21.0", "pytest-cov>=4.1.0"]
dev = ["ruff>=0.1.0", "invoke>=2.2.0", "pre-commit>=3.5.0"]
```

Spin up: `uv sync --extra app`. Run tests: `uv run pytest`. Add a dependency: `uv add httpx`. No `pip install -e .`, no activation ceremony, no `requirements.txt` drift. The lockfile (`uv.lock`) pins everything deterministically. `uv sync --frozen` in CI installs from the lockfile without re-resolving.

A cold sync of the full dependency tree — 40-odd packages including Playwright — takes under 10 seconds. Transporter beam, not turbolift.

## Python 3.15: The Refit Enterprise

Python 3.15 is the most substantive release since 3.10 added structural pattern matching. Here are the features that actually show up in EventLoop.

<div id="pep-cards" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin:2rem 0;font-family:'Space Grotesk',sans-serif;"><noscript><ul><li>⚡ <strong>PEP 810 — Lazy Imports</strong>: <code>lazy from foo import bar</code> — deferred loading, zero cost if unused</li><li>🧊 <strong>PEP 814 — frozendict</strong>: Immutable, hashable dicts as a built-in. No more MappingProxyType.</li><li>🏴 <strong>PEP 661 — sentinel</strong>: Named sentinel values with useful reprs. <code>sentinel('MISSING')</code></li><li>☄️ <strong>PEP 799 — Tachyon</strong>: Statistical sampling profiler in stdlib. Zero instrumentation overhead.</li><li>🚀 <strong>PEP 686 — UTF-8 mode</strong>: UTF-8 default everywhere. No more locale surprises.</li><li>📦 <strong>PEP 798 — Unpack in Comprehensions</strong>: <code>[*sublist for sublist in nested]</code> — flatten without itertools.</li></ul></noscript></div>
<script>
(function(){
  var peps=[
    {id:"PEP 810",name:"Lazy Imports",desc:"lazy from foo import bar — deferred loading, zero cost if unused",icon:"⚡"},
    {id:"PEP 814",name:"frozendict",desc:"Immutable, hashable dicts as a built-in. No more MappingProxyType.",icon:"🧊"},
    {id:"PEP 661",name:"sentinel",desc:"Named sentinel values with useful reprs. sentinel('MISSING')",icon:"🏴"},
    {id:"PEP 686",name:"UTF-8 Default",desc:"UTF-8 everywhere, always, without PYTHONUTF8=1",icon:"🌐"},
    {id:"PEP 799",name:"Tachyon",desc:"Statistical sampling profiler in stdlib. Zero instrumentation overhead.",icon:"☄️"},
    {id:"PEP 798",name:"Unpack in Comprehensions",desc:"[*sublist for sublist in nested] — flatten without itertools",icon:"📦"},
  ];
  var container=document.getElementById('pep-cards');
  peps.forEach(function(p,i){
    var card=document.createElement('div');
    card.style.cssText='background:#0f172a;border:1px solid #1e293b;border-radius:0.75rem;padding:1.25rem;position:relative;overflow:hidden;transition:border-color 0.2s,transform 0.2s;cursor:default;';
    card.innerHTML='<div style="font-size:1.75rem;margin-bottom:0.5rem">'+p.icon+'</div>'
      +'<div style="font-size:0.65rem;color:#059669;font-weight:700;letter-spacing:0.1em;margin-bottom:0.25rem">'+p.id+'</div>'
      +'<div style="font-size:0.95rem;color:#f1f5f9;font-weight:600;margin-bottom:0.5rem">'+p.name+'</div>'
      +'<div style="font-size:0.78rem;color:#94a3b8;line-height:1.5">'+p.desc+'</div>'
      +'<div style="position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#059669,#0ea5e9);opacity:0;transition:opacity 0.2s" class="card-line"></div>';
    card.addEventListener('mouseenter',function(){
      this.style.borderColor='#059669';
      this.style.transform='translateY(-2px)';
      this.querySelector('.card-line').style.opacity='1';
    });
    card.addEventListener('mouseleave',function(){
      this.style.borderColor='#1e293b';
      this.style.transform='';
      this.querySelector('.card-line').style.opacity='0';
    });
    // stagger appearance
    card.style.opacity='0';
    card.style.transform='translateY(12px)';
    container.appendChild(card);
    setTimeout(function(c){ c.style.transition='opacity 0.4s ease,transform 0.4s ease,border-color 0.2s,transform 0.2s'; c.style.opacity='1'; c.style.transform='translateY(0)'; },100+i*80,card);
  });
})();
</script>

### PEP 810: Explicit Lazy Imports

This one matters most for AI tooling. Python 3.15 adds `lazy` as a soft keyword — deferred module loading until the name is first used:

```python
# Before 3.15: every import evaluated at module load time
from app.chat.agent import agent            # loads PydanticAI, Anthropic SDK, ...
from app.chat.intent_classifier import IntentClassifier  # loads more
from shared.database import AsyncSessionLocal            # triggers SQLAlchemy

# With lazy imports in 3.15 — the `lazy` soft keyword:
lazy from app.chat.agent import agent
lazy from app.chat.intent_classifier import IntentClassifier
lazy from shared.database import AsyncSessionLocal
# Each module loads only when its name is first referenced
```

When your FastAPI lifespan hook is the only place the agent runs, you don't need its dependencies loaded during test collection or scraper subprocess startup. Both `lazy import foo` and `lazy from foo import bar` work. It's a soft keyword, so existing code named `lazy` doesn't break.

One thing the PEP doesn't warn you about loudly enough: `lazy` changes module initialization order, and that will find your latent circular imports. EventLoop had one — `web_search.py` imports `SearchPolicy` from `chatbot.py`, and `chatbot.py` re-exports `EventResult` back from `web_search.py`. It never fired, because an eager `from app.chat.chatbot import ...` in `executor.py` always warmed `sys.modules` first. The moment that line became `lazy from`, the warm-up vanished and test collection died on an `ImportError` from a partially initialized module.

The fix was to move `SearchPolicy` into a third module, `policy.py`, that both files import from — so neither needs the other. The cycle was always there. Eager imports were hiding it. That's the honest version of "free wins, no code changes" — the wins are free, but `lazy from` is a load-bearing change to *when* your modules run, and the bug it surfaces was yours all along.

### PEP 814: `frozendict` Built-in

EventLoop has a neighborhood alias mapping — computed once at startup, never mutated. Pre-3.15, you'd use `types.MappingProxyType` and fight the type checker. Now:

```python
NEIGHBORHOOD_ALIASES: frozendict[str, str] = frozendict({
    "wicker park": "Wicker Park",
    "logan sq": "Logan Square",
    "the loop": "Loop",
})
```

`frozendict` is hashable, genuinely immutable at runtime, and visible to your editor and type checker. No more silent mutations corrupting global state between requests.

### PEP 661: `sentinel` Built-in

The sentinel pattern is everywhere in Python — distinguishing "not provided" from `None`, default markers, missing values. 3.15 formalizes it:

```python
# sentinel is a built-in in 3.15 — no import needed, just like frozendict
MISSING = sentinel("MISSING")

def get_event_cost(event: EventResult, default=MISSING) -> str | None:
    if event.cost is None:
        if default is MISSING:
            raise ValueError("cost not set and no default provided")
        return default
    return event.cost
```

Pre-3.15, `_MISSING = object()` would print as `<object object at 0x10b3f2d30>` in every traceback. `sentinel("MISSING")` has a name and a repr. Like `frozendict`, it's a built-in — no import statement required.

### PEP 686: UTF-8 as Default Encoding

Finally. Python now defaults to UTF-8 everywhere without `PYTHONUTF8=1` or `encoding="utf-8"` on every `open()`. For a scraper reading HTML from Chicago venue sites — which contain em-dashes, curly quotes, and the occasional stray `\u2019` in event names — this eliminates a whole class of bugs that only appeared on Windows CI runners.

### PEP 799: Tachyon — Profiling Package

Named after the faster-than-light particles from *The Next Generation* that appear whenever the writers needed to violate causality. The `profiling` package in Python 3.15's standard library reorganizes all built-in profilers:

- `profiling.tracing` — deterministic tracing (replaces `cProfile`, which still works as an alias)
- `profiling.sampling` — **Tachyon**, a statistical sampling profiler with zero instrumentation overhead

```bash
# Tracing profiler (high overhead, exact counts):
python -m profiling.tracing my_script.py

# Tachyon sampling (zero overhead, can attach to production processes):
python -m profiling.sampling my_script.py
```

For an async chatbot where I was puzzled about latency between the intent classifier, local DB search, and the PydanticAI agent loop, `profiling.sampling` is the right tool: no `cProfile` distortion of the async event loop, works on multiple threads, and can attach to a running process. The old `profile` module is deprecated in 3.15 (removal in 3.17).

### JIT: 7–8% on x86-64, 11–12% on AArch64

Per the [release announcement](https://blog.python.org/2026/10/python-3150-final-is-here): the experimental JIT compiler has been significantly upgraded with **7–8% geometric mean performance improvement on x86-64 Linux** over the standard interpreter, and **11–12% speedup on AArch64 macOS** over the tail-calling interpreter. The Railway API service runs on Linux x86-64. The wins in EventLoop live in synchronous CPU-bound work: regex matching in the intent classifier, semantic embedding lookups, neighborhood polygon intersection. Free perf, no code changes.

<canvas id="jit-chart" width="600" height="240" style="width:100%;max-width:600px;display:block;margin:2rem auto;border-radius:0.75rem;background:#0f172a;border:1px solid #1e293b;"></canvas>
<noscript><table><caption>Python 3.15 JIT — geometric mean speedup over baseline interpreter</caption><thead><tr><th>Platform</th><th>Speedup</th><th>Baseline</th></tr></thead><tbody><tr><td>x86-64 Linux (Railway API service)</td><td>+7–8%</td><td>vs standard interpreter</td></tr><tr><td>AArch64 macOS (M-series Mac / ARM CI)</td><td>+11–12%</td><td>vs tail-calling interpreter</td></tr></tbody></table></noscript>
<script>
(function(){
  var canvas=document.getElementById('jit-chart');
  var ctx=canvas.getContext('2d');
  var dpr=window.devicePixelRatio||1;
  canvas.width=600*dpr; canvas.height=240*dpr;
  canvas.style.width='100%'; canvas.style.maxWidth='600px';
  ctx.scale(dpr,dpr);
  var W=600,H=240;
  // Two bars only — baseline is the 0% reference line, not an empty bar
  var bars=[
    {label:'x86-64 Linux',sub:'(Railway API service)',color:'#059669',lo:7,hi:8,baseline:'vs standard interpreter'},
    {label:'AArch64 macOS',sub:'(M-series Mac / ARM CI)',color:'#0ea5e9',lo:11,hi:12,baseline:'vs tail-calling interpreter'},
  ];
  var maxVal=15,padL=44,padR=24,padT=44,padB=72;
  var barW=(W-padL-padR)/bars.length;
  var chartH=H-padT-padB;
  var start=null;
  function ease(t){return t<0.5?2*t*t:1-Math.pow(-2*t+2,2)/2;}
  function draw(ts){
    if(!start)start=ts;
    var prog=Math.min((ts-start)/1000,1);
    var e=ease(prog);
    ctx.clearRect(0,0,W,H);
    // Title
    ctx.fillStyle='#94a3b8';
    ctx.font='600 12px "Space Grotesk",sans-serif';
    ctx.textAlign='center';
    ctx.fillText('Python 3.15 JIT — geometric mean speedup over baseline interpreter',W/2,20);
    // Gridlines + y-axis labels
    [0,5,10,15].forEach(function(v){
      var y=padT+chartH-(v/maxVal)*chartH;
      ctx.strokeStyle=v===0?'#475569':'#1e293b';
      ctx.lineWidth=v===0?1.5:1;
      ctx.setLineDash(v===0?[]:[4,3]);
      ctx.beginPath(); ctx.moveTo(padL,y); ctx.lineTo(W-padR,y); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle='#475569'; ctx.font='10px monospace'; ctx.textAlign='right';
      ctx.fillText(v+'%',padL-6,y+4);
    });
    // Baseline label
    ctx.fillStyle='#475569'; ctx.font='9px monospace'; ctx.textAlign='left';
    ctx.fillText('← baseline (3.14)',padL+4,padT+chartH-4);
    // Bars with range shading
    bars.forEach(function(b,i){
      var x=padL+i*barW;
      var bw=barW*0.45, bx=x+(barW-bw)/2;
      // Range band (lo to hi)
      var yHi=padT+chartH-(b.hi/maxVal)*chartH*e;
      var yLo=padT+chartH-(b.lo/maxVal)*chartH*e;
      var bandH=yLo-yHi;
      // Main bar to midpoint
      var mid=(b.lo+b.hi)/2;
      var yMid=padT+chartH-(mid/maxVal)*chartH*e;
      var barH=padT+chartH-yMid;
      // Glow
      ctx.shadowColor=b.color; ctx.shadowBlur=14;
      ctx.fillStyle=b.color;
      var rx=5;
      ctx.beginPath();
      ctx.moveTo(bx+rx,yMid); ctx.lineTo(bx+bw-rx,yMid);
      ctx.quadraticCurveTo(bx+bw,yMid,bx+bw,yMid+rx);
      ctx.lineTo(bx+bw,padT+chartH); ctx.lineTo(bx,padT+chartH);
      ctx.lineTo(bx,yMid+rx);
      ctx.quadraticCurveTo(bx,yMid,bx+rx,yMid);
      ctx.fill();
      ctx.shadowBlur=0;
      // Range bracket overlay
      if(e>0.6){
        var ralpha=Math.min((e-0.6)/0.4,1);
        ctx.fillStyle=b.color;
        ctx.globalAlpha=ralpha*0.25;
        ctx.fillRect(bx,yHi,bw,bandH);
        ctx.globalAlpha=1;
        // Bracket lines
        ctx.strokeStyle=b.color; ctx.lineWidth=1.5; ctx.globalAlpha=ralpha*0.8;
        ctx.beginPath(); ctx.moveTo(bx+bw*0.2,yHi); ctx.lineTo(bx+bw*0.8,yHi); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(bx+bw*0.2,yLo); ctx.lineTo(bx+bw*0.8,yLo); ctx.stroke();
        ctx.globalAlpha=1;
        // Range label
        ctx.fillStyle=b.color; ctx.font='bold 13px "Space Grotesk",sans-serif'; ctx.textAlign='center';
        ctx.fillText('+'+b.lo+'–'+b.hi+'%',bx+bw/2,yHi-8);
      }
      // X labels
      ctx.fillStyle='#94a3b8'; ctx.font='11px "Space Grotesk",sans-serif'; ctx.textAlign='center';
      ctx.fillText(b.label,bx+bw/2,padT+chartH+18);
      ctx.fillStyle='#475569'; ctx.font='9px "Space Grotesk",sans-serif';
      ctx.fillText(b.sub,bx+bw/2,padT+chartH+32);
      ctx.fillStyle=b.color; ctx.font='9px monospace';
      ctx.fillText(b.baseline,bx+bw/2,padT+chartH+46);
    });
    // Source
    ctx.fillStyle='#334155'; ctx.font='9px monospace'; ctx.textAlign='center';
    ctx.fillText('Source: docs.python.org/3.15/whatsnew/3.15.html · blog.python.org',W/2,H-8);
    if(prog<1) requestAnimationFrame(draw);
  }
  if('IntersectionObserver' in window){
    var obs=new IntersectionObserver(function(entries){
      if(entries[0].isIntersecting){obs.disconnect();requestAnimationFrame(draw);}
    },{threshold:0.3});
    obs.observe(canvas);
  } else { requestAnimationFrame(draw); }
})();
</script>

## 3.15 vs 3.14: The Honest Comparison

| Feature | Python 3.14 | Python 3.15 |
|---|---|---|
| Immutable dicts | `MappingProxyType` workaround | `frozendict` built-in, hashable, typed |
| Sentinel values | `object()` with bad reprs | `sentinel()` built-in, named, inspectable |
| Default encoding | Platform-dependent, CI surprises | UTF-8 everywhere |
| Startup time | All imports eager | `lazy import` / `lazy from` soft keyword |
| Profiling | `cProfile` or third-party | `profiling.sampling` (Tachyon) in stdlib |
| JIT performance | Marginal | 7-12% geometric mean |

3.14 → 3.15 is less dramatic than 3.9 → 3.10 (pattern matching). But it's a *quality* release. The things it adds are things you've been reaching for and finding absent: immutable dicts, named sentinels, UTF-8 sanity, lazy loading. Not flashy. Correct.

## Why PydanticAI — And Why 3.15 Makes It Better

I get asked about agent frameworks constantly. My answer is PydanticAI, for reasons that became obvious building EventLoop: typed output, cloud-agnostic model selection, tests that run without a paid API call, and — critically for a streaming SSE API — it gets out of the way. The agent runs, the tools run, the executor yields events. No framework magic in the stream path.

EventLoop's agent is typed end-to-end:

```python
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.anthropic import AnthropicModel
from app.chat.chatbot import SearchPolicy, search_local_db
from app.chat.web_search import search_google_events

agent = Agent(
    model=AnthropicModel("claude-sonnet-5-5"),
    system_prompt=SYSTEM_PROMPT,
    deps_type=SearchPolicy,
)

@agent.tool
async def search_db(ctx: RunContext[SearchPolicy], query: str) -> list[EventResult]:
    return await search_local_db(query, policy=ctx.deps)

@agent.tool
async def web_fallback(ctx: RunContext[SearchPolicy], query: str) -> list[EventResult]:
    return await search_google_events(query)
```

`SearchPolicy` is a Pydantic model. Tool return types are Pydantic models. The agent validates tool arguments before they run. My editor knows the shape of every input and output. I can test without calling Anthropic (`pydantic_ai.models.test.TestModel` runs the full loop against a fake model). The model is a string I pass in, so switching providers doesn't touch tool definitions.

Add Python 3.15 and the next round of cleanups writes itself: `frozendict` for the neighborhood alias lookup in `neighborhoods.py`, so it's immutable at runtime and not just by convention; `lazy from` on the agent and intent classifier imports in `executor.py`; `sentinel` for the "field not returned vs. returned as null" distinction in `EventResult`. None of these are load-bearing on their own. They're the kind of small wins that compound.

## The Three-Tier Architecture: Agentic Thinking Made Concrete

The part I'm most proud of isn't the agent — it's what *gates* it. Running Claude Sonnet on every message is expensive. The solution is a three-tier routing pipeline:

```
User message
    ↓
[1] Regex fast-path → CHICAGO_EVENTS (zero LLM cost)
    ↓ (if ambiguous)
[2] Claude Haiku intent classifier (~30× cheaper per token than Sonnet)
    → CHICAGO_EVENTS | CHICAGO_INFO | EVENTS_GENERAL | OUT_OF_SCOPE | FAREWELL
    ↓ (if event-related)
[3] Claude Sonnet via PydanticAI agent
    → search_local_db → search_google_events (fallback when local is thin)
```

The Haiku classifier returns a structured `IntentClassification` model — confidence score included. High confidence routes through. Low confidence gets a clarification prompt.

<div id="routing-diagram" style="margin:2rem auto;max-width:560px;"><noscript><pre>
User message
    ↓
[1] Regex fast-path → CHICAGO_EVENTS (zero LLM cost)
    ↓ (if ambiguous)
[2] Claude Haiku intent classifier (~30× cheaper per token than Sonnet)
    → CHICAGO_EVENTS | CHICAGO_INFO | EVENTS_GENERAL | OUT_OF_SCOPE | FAREWELL
    ↓ (if event-related)
[3] Claude Sonnet via PydanticAI agent
    → search_local_db → search_google_events (fallback when local is thin)
</pre></noscript></div>
<script>
(function(){
  var container=document.getElementById('routing-diagram');
  var nodes=[
    {id:'msg',   label:'User Message',        sub:'POST /api/chat',          color:'#334155', text:'#f1f5f9', y:0},
    {id:'regex', label:'① Regex Fast-Path',   sub:'zero LLM cost',           color:'#059669', text:'#fff',    y:1},
    {id:'haiku', label:'② Haiku Classifier',  sub:'~$0.0001/call',           color:'#0ea5e9', text:'#fff',    y:2},
    {id:'agent', label:'③ Sonnet Agent',      sub:'PydanticAI · ~$0.003/call',color:'#7c3aed', text:'#fff',  y:3},
    {id:'tools', label:'search_local_db  +  search_google_events', sub:'SQL → semantic rerank → top-5 results', color:'#1e293b', text:'#94a3b8', y:4},
  ];
  var W=560,nodeH=52,nodeW=420,gap=32,arrowH=gap;
  var totalH=nodes.length*(nodeH+gap)+40;
  var svg='<svg viewBox="0 0 '+W+' '+totalH+'" xmlns="http://www.w3.org/2000/svg" style="width:100%;display:block;">';
  svg+='<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M1,1 L7,4 L1,7 Z" fill="#475569"/></marker></defs>';
  nodes.forEach(function(n,i){
    var x=(W-nodeW)/2;
    var y=20+i*(nodeH+gap);
    // draw arrow from previous node
    if(i>0){
      var prevY=20+(i-1)*(nodeH+gap)+nodeH;
      var midY=prevY+gap/2;
      svg+='<line x1="'+W/2+'" y1="'+prevY+'" x2="'+W/2+'" y2="'+(y-8)+'" stroke="#475569" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arr)"/>';
    }
    // node rect
    var r=8;
    svg+='<rect x="'+x+'" y="'+y+'" width="'+nodeW+'" height="'+nodeH+'" rx="'+r+'" fill="'+n.color+'" opacity="0.95"/>';
    // side accent line
    svg+='<rect x="'+x+'" y="'+(y+8)+'" width="3" height="'+(nodeH-16)+'" rx="1.5" fill="#059669" opacity="'+(n.color==='#059669'?'0':'0.7')+'"/>';
    // label
    svg+='<text x="'+(x+20)+'" y="'+(y+nodeH/2-6)+'" font-family="Space Grotesk,sans-serif" font-size="13" font-weight="600" fill="'+n.text+'" dominant-baseline="middle">'+n.label+'</text>';
    svg+='<text x="'+(x+20)+'" y="'+(y+nodeH/2+12)+'" font-family="Space Grotesk,sans-serif" font-size="10" fill="'+(n.text==='#fff'?'rgba(255,255,255,0.6)':'#475569')+'" dominant-baseline="middle">'+n.sub+'</text>';
    // bypass labels on arrow
    if(i===1){
      svg+='<text x="'+(W/2+8)+'" y="'+(20+nodeH+gap/2)+'" font-size="9" fill="#059669" font-family="Space Grotesk,sans-serif">match → skip LLM</text>';
    }
    if(i===2){
      svg+='<text x="'+(W/2+8)+'" y="'+(20+(nodeH+gap)+nodeH+gap/2)+'" font-size="9" fill="#0ea5e9" font-family="Space Grotesk,sans-serif">event-related → agent</text>';
    }
  });
  svg+='</svg>';
  container.innerHTML=svg;
  // fade-in on scroll
  container.style.opacity='0';
  container.style.transform='translateY(16px)';
  container.style.transition='opacity 0.5s ease,transform 0.5s ease';
  if('IntersectionObserver' in window){
    new IntersectionObserver(function(entries,obs){
      if(entries[0].isIntersecting){
        container.style.opacity='1'; container.style.transform='';
        obs.disconnect();
      }
    },{threshold:0.2}).observe(container);
  } else { container.style.opacity='1'; container.style.transform=''; }
})();
</script>

Building this pipeline is where agentic coding became concrete for me. I directed an AI pair programmer (Cline, running Claude) to build the initial classifier. I reviewed the output. I caught the subtle bugs — the farewell classifier kept marking "anything cheaper?" as a farewell because "appreciate it" scored positive sentiment. Sentiment and intent are not the same thing.

The docstring in `intent_classifier.py` now says it plainly:

```
"👍"                                positive  -> farewell
"no worries, I'll figure it out"    neutral   -> farewell
"cool cool cool"                    positive  -> farewell
"appreciate it - anything cheaper?" positive  -> NOT farewell
"ugh, nothing good on then?"        negative  -> NOT farewell
```

Two positives on opposite sides and a negative that's still a request. The model wrote the code; I did the thinking.

That's the skill shift from my first post: less syntax, more strategy.

## One Python Version. For Everything.

EventLoop runs **Python 3.15 for both the API and the scraper**. This wasn't always the plan — when I started, the scraper was pinned to 3.14 because `greenlet` (a SQLAlchemy dependency) didn't have cp315 wheels yet, and the Microsoft `playwright/python` Docker image hard-codes its own Python version.

Both blockers are gone. `greenlet 3.5.6` (released September 14, 2026) ships full `cp315-manylinux` wheels. `playwright 1.63.0` is `py3-none` — pure Python, any version. And we dropped the Microsoft base image entirely: the scraper now uses `python:3.15.0rc3-slim` and installs Playwright's Chromium browser binary itself:

```dockerfile
FROM python:3.15.0rc3-slim
# (python:3.15-slim once Docker Hub publishes the final tag)

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libc6-dev \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 \
    libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 \
    libpango-1.0-0 libcairo2 libasound2t64 libatspi2.0-0 ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv==0.12.24
COPY pyproject.toml uv.lock ./
# The scraper only needs the `parser` extra — `app` pulls in uvicorn[standard]
# which requires gcc to build httptools from source (no cp315 wheel yet).
RUN uv sync --frozen --extra parser --no-dev --no-install-project
RUN uv run playwright install chromium
```

One Python version. One lockfile. No subprocess boundary. No "which environment is this running in?" when a bug appears at 2am.

The extras story is sharpest here: `--extra parser` excludes the entire FastAPI and PydanticAI stacks from the scraper image. They're not installed at all — so they cost zero import time, not just lazy-deferred time. uv's dependency groups do the work before the process even starts.

## Zero Ruff Errors, Every Suppression Documented

The project has zero ruff errors across `src/`, `tests/`, `scripts/`, and `eval/`. Every suppression is *explained*:

```toml
# Scrapers construct naive datetimes intentionally: event dates are stored as
# local-midnight naive values. Timezone-aware datetimes would require migrating
# the entire events table and all downstream comparisons.
"src/scrapers/**" = ["DTZ", ...]
```

A `noqa` comment nobody can explain is a landmine for future-you. Document the *why*.

## Actually Shipping It: Railway + PostgreSQL

Three services, one Railway project, one PostgreSQL database — 90 neighborhoods, 68 venues, events growing every six hours:

- **`api`** — Python 3.15, FastAPI, always-on, `rootDirectory=backend`, picks up `Dockerfile` and `railway.toml` automatically
- **`frontend`** — nginx, `rootDirectory=frontend`. Proxies `/api/*` to the backend via `envsubst` at container start — `${API_URL}` gets substituted into the nginx config at runtime, so no rebuild needed when the backend URL changes
- **`scraper`** — Python 3.15 + Playwright, cron `0 */6 * * *`, separate `Dockerfile.scraper` pointed at `railway.scraper.toml`

The whole thing is live at **[eventloop.city](https://eventloop.city)** — custom domain on Porkbun, ALIAS `@` → Railway, SSL auto-provisioned by Let's Encrypt through Railway. Go find something to do in Chicago.

<div id="arch-diagram" style="margin:2rem auto;max-width:600px;"><noscript><pre>
                    EventLoop on Railway

  ┌─────────────┐   /api/* proxy   ┌──────────────────┐     ┌───────────────────────┐
  │  frontend   │ ────────────────▶ │       api        │     │       scraper         │
  │ nginx·Vite  │                  │ FastAPI·Python3.15│     │ Playwright·cron 0*/6  │
  └─────────────┘                  └────────┬─────────┘     └──────────┬────────────┘
                                            │                           │
                                            └───────────┬───────────────┘
                                                        ▼
                                            ┌───────────────────────┐
                                            │       PostgreSQL       │
                                            │ Chicago events · 90   │
                                            │ neighborhoods · ~$12/mo│
                                            └───────────────────────┘
</pre></noscript></div>
<script>
(function(){
  var container=document.getElementById('arch-diagram');
  var W=600,H=320;
  var svg='<svg viewBox="0 0 '+W+' '+H+'" xmlns="http://www.w3.org/2000/svg" style="width:100%;display:block;">';
  // Defs first so markers are defined before use
  svg+='<defs>'
     +'<marker id="db-arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M1,1 L7,4 L1,7 Z" fill="#475569"/></marker>'
     +'<marker id="h-arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M1,1 L7,4 L1,7 Z" fill="#059669"/></marker>'
     +'</defs>';
  // Background
  svg+='<rect width="'+W+'" height="'+H+'" rx="12" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>';
  svg+='<text x="'+W/2+'" y="26" text-anchor="middle" font-family="Space Grotesk,sans-serif" font-size="12" fill="#475569" font-weight="600">EventLoop on Railway</text>';

  // Services top row
  var services=[
    {label:'frontend',sub:'nginx · Vite/TS',color:'#1e40af',icon:'🌐',x:80},
    {label:'api',     sub:'FastAPI · Python 3.15',color:'#059669',icon:'⚡',x:280},
    {label:'scraper', sub:'Playwright · cron 0 */6 * * *',color:'#7c3aed',icon:'🕷️',x:480},
  ];
  var sW=130,sH=70,sY=60;
  services.forEach(function(s){
    var sx=s.x-sW/2;
    svg+='<rect x="'+sx+'" y="'+sY+'" width="'+sW+'" height="'+sH+'" rx="8" fill="'+s.color+'" opacity="0.15" stroke="'+s.color+'" stroke-width="1.5"/>';
    svg+='<text x="'+s.x+'" y="'+(sY+22)+'" text-anchor="middle" font-size="18">'+s.icon+'</text>';
    svg+='<text x="'+s.x+'" y="'+(sY+42)+'" text-anchor="middle" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" fill="#f1f5f9">'+s.label+'</text>';
    svg+='<text x="'+s.x+'" y="'+(sY+56)+'" text-anchor="middle" font-family="Space Grotesk,sans-serif" font-size="9" fill="'+s.color+'">'+s.sub+'</text>';
  });

  // Postgres box
  var dbW=160,dbH=56,dbX=(W-dbW)/2,dbY=220;
  svg+='<rect x="'+dbX+'" y="'+dbY+'" width="'+dbW+'" height="'+dbH+'" rx="8" fill="#b45309" opacity="0.15" stroke="#b45309" stroke-width="1.5"/>';
  svg+='<text x="'+W/2+'" y="'+(dbY+20)+'" text-anchor="middle" font-size="16">🐘</text>';
  svg+='<text x="'+W/2+'" y="'+(dbY+36)+'" text-anchor="middle" font-family="Space Grotesk,sans-serif" font-size="12" font-weight="700" fill="#f1f5f9">PostgreSQL</text>';
  svg+='<text x="'+W/2+'" y="'+(dbY+50)+'" text-anchor="middle" font-family="Space Grotesk,sans-serif" font-size="9" fill="#b45309">Chicago events · 90 neighborhoods · scraper every 6h</text>';

  // Arrows: api + scraper → postgres (frontend/nginx does not speak Postgres)
  services.filter(function(s){return s.label!=='frontend';}).forEach(function(s){
    var x1=s.x, y1=sY+sH;
    var x2=W/2, y2=dbY;
    svg+='<path d="M'+x1+','+y1+' C'+x1+','+(y1+40)+' '+x2+','+(y2-40)+' '+x2+','+y2+'" fill="none" stroke="'+s.color+'" stroke-width="1.5" stroke-dasharray="5 3" opacity="0.7" marker-end="url(#db-arr)"/>';
  });

  // Arrow: frontend → api (HTTP proxy)
  var midY=sY+sH/2;
  svg+='<line x1="'+(80+sW/2)+'" y1="'+midY+'" x2="'+(280-sW/2)+'" y2="'+midY+'" stroke="#059669" stroke-width="1.5" marker-end="url(#h-arr)"/>';
  svg+='<text x="180" y="'+(midY-6)+'" text-anchor="middle" font-size="8" fill="#059669" font-family="Space Grotesk,sans-serif">/api/* proxy</text>';

  // Legend
  svg+='<text x="16" y="'+(H-12)+'" font-size="9" fill="#334155" font-family="monospace">asyncpg · asyncio · SQLAlchemy 2.0 · ~$10–12/month on Railway Hobby</text>';

  svg+='</svg>';
  container.innerHTML=svg;
  container.style.opacity='0';
  container.style.transition='opacity 0.6s ease';
  if('IntersectionObserver' in window){
    new IntersectionObserver(function(e,o){if(e[0].isIntersecting){container.style.opacity='1';o.disconnect();}},{threshold:0.2}).observe(container);
  } else { container.style.opacity='1'; }
})();
</script>

All three connect to the same Railway PostgreSQL service via `${{Postgres.DATABASE_URL}}`. One thing I learned: Railway can inject that URL as `postgresql+psycopg://` (the sync psycopg3 dialect), not just plain `postgresql://`. The fix is to normalise before SQLAlchemy sees it:

```python
def _normalise_db_url(url: str) -> str:
    for prefix, replacement in [
        ("postgresql+psycopg2://", "postgresql+asyncpg://"),
        ("postgresql+psycopg://",  "postgresql+asyncpg://"),
        ("postgres://",            "postgresql+asyncpg://"),
        ("postgresql://",          "postgresql+asyncpg://"),
    ]:
        if url.startswith(prefix):
            return replacement + url[len(prefix):]
    return url
```

And after migrating from local SQLite to Railway Postgres: Postgres sequences. A bulk migration that inserts rows with explicit IDs doesn't advance the `SERIAL` sequence — every new `INSERT` hits a unique-key collision. Fixed with `setval(pg_get_serial_sequence(...), MAX(id))` on each table. Ship an admin endpoint for this, not a one-liner you have to remember.

Everything else (build config, healthcheck path, cron schedule, restart policy) lives in committed `railway.toml` files alongside the Dockerfiles. Total cost: ~$10–12/month on the Hobby plan. The Anthropic API bill is separate and scales with actual usage.

## Stardate 2026.282: Ship It

Python 3.15.0 final [dropped today](https://blog.python.org/2026/10/python-3150-final-is-here) — October 9th, 2026 — from release manager Hugo van Kemenade, with Ned Deily and Steve Dower on the release team. 5,643 commits from **1,012 contributors**. As a former PSF Chairperson, I never get tired of reading that number. Open source at scale.

To celebrate, Barry Warsaw shipped [`whatsnewt`](https://pypi.org/project/whatsnewt/) — a TUI text adventure through What's New in Python 3.15. Eighteen puzzles, each one a real 3.15 feature you have to actually write and run code to solve. Type checking verified by `pyrefly`. Easter eggs. Run it:

```bash
uvx --python 3.15 whatsnewt
```

You wake up in the Startup Foyer, inside the interpreter, and work your way to the Release Gate. It's exactly the kind of thing that makes me proud to be part of this community.

uv 0.12.24 is ready. Here's what I'd tell you starting a Python project today:

1. **Use uv.** The toolchain friction it removes is real and immediate. `uv sync --frozen` in CI, `uv run` for everything else.
2. **Pin Python 3.15.** `frozendict`, `sentinel`, UTF-8 everywhere, `lazy` imports — right answers the language needed for a decade.
3. **Use PydanticAI for agent work.** Typed output is not optional when calling LLMs in production and you want tests that don't burn API credits.
4. **Build the cheapest gate first.** A Haiku intent classifier at ~$0.0001/call vs $0.003 for Sonnet is a 30× win you can see in your billing dashboard.
5. **Let the AI pair programmer scaffold. Review it like a junior engineer's PR.** The skill is in the review, not the typing.
6. **Postgres in production, not SQLite.** You will hit sequence desync and you will hit it at the worst time.

The Enterprise got refitted between films. Upgraded nacelles, better computers, same crew with the same values and better tools. Python 3.15 + uv is that: the language and toolchain we already know, refit for the work we're actually doing now. The mission hasn't changed. The ship is just better.

Live long, Python & prosper. 🖖

---

<script>
(function(){
  // ── EASTER EGG 1: Console greeting ────────────────────────────────────────
  var NCC=[
    '                               . *  |  * .',
    '        _______________________|____|____|_______________________',
    '       /_______________________________________________NCC-1701-D\\',
    '      /  _____   _______  |  __|__  |  _______   _____  \\',
    '==== /  / WARP\\_/ DRIVE \\ | /EVENT\\ | /PYTHON \\_/ 3.15 \\  \\ ====',
    '      \\  \\_____/ \\_______/ | \\LOOP/ | \\_______/ \\_____/  /',
    '       \\________________________________________________ /',
    '                     |                  |',
    '                   __|__              __|__',
    '                  / NAC \\            / NAC \\',
    '                 /_______\\          /_______\\',
  ].join('\n');
  var QUOTES=[
    '"It is possible to commit no mistakes and still lose. That is not weakness, that is life." — Picard',
    '"I am fully functional, programmed in multiple techniques." — Data',
    '"Things are only impossible until they\'re not." — Picard',
    '"Make it so." — Picard (also: git push origin main)',
    '"Resistance is futile." — The Borg (also: uv over pip)',
  ];
  var q=QUOTES[Math.floor(Math.random()*QUOTES.length)];
  var g=console.log.bind(console);
  g('%c','font-size:1px');
  g('%c  NCC-1701-D  ','background:#FF9900;color:#000;font-weight:bold;font-size:14px;padding:4px 12px;border-radius:3px;font-family:monospace;letter-spacing:2px');
  g('%c'+NCC,'color:#9999FF;font-family:monospace;font-size:11px;line-height:1.5');
  g('%c'+q,'color:#FF9900;font-family:monospace;font-size:12px;font-style:italic;padding:8px 0');
  g('%c  STARDATE 2026.282 · SECTOR CHICAGO-ILL · PYTHON 3.15 ONLINE  ','color:#44CC44;font-family:monospace;font-size:10px;letter-spacing:1px');
  g('%c  eventloop.city · github.com/lorenanicole/event-loop  ','color:#475569;font-family:monospace;font-size:10px');
  g('%c','font-size:1px');
})();
</script>

<script>
(function(){
  // ── EASTER EGG 2: Type "llap" → warp speed starfield ─────────────────────
  var TYPED='',TARGET='llap',warpActive=false;
  document.addEventListener('keydown',function(e){
    if(warpActive)return;
    TYPED+=e.key.toLowerCase();
    if(TYPED.length>TARGET.length)TYPED=TYPED.slice(-TARGET.length);
    if(TYPED===TARGET){TYPED='';fireWarp();}
  });
  function fireWarp(){
    warpActive=true;
    var canvas=document.createElement('canvas');
    canvas.style.cssText='position:fixed;top:0;left:0;width:100%;height:100%;z-index:9999;pointer-events:none;';
    canvas.width=window.innerWidth;canvas.height=window.innerHeight;
    document.body.appendChild(canvas);
    var ctx=canvas.getContext('2d'),W=canvas.width,H=canvas.height,cx=W/2,cy=H/2;
    var overlay=document.createElement('div');
    overlay.style.cssText='position:fixed;top:0;left:0;width:100%;height:100%;z-index:10000;pointer-events:none;display:flex;flex-direction:column;align-items:center;justify-content:center;';
    var qEl=document.createElement('div');
    qEl.style.cssText='font-family:monospace;font-size:clamp(13px,2vw,20px);color:#FF9900;text-align:center;padding:2rem;max-width:560px;opacity:0;transition:opacity 0.6s;text-shadow:0 0 20px #FF9900;';
    qEl.innerHTML='🖖 <em>Live long, Python &amp; prosper.</em> 🖖<br><span style="font-size:0.7em;color:#9999FF;margin-top:0.5rem;display:block">LLAP · NCC-1701-D · STARDATE 2026.282</span>';
    overlay.appendChild(qEl);document.body.appendChild(overlay);
    var stars=[];
    for(var i=0;i<220;i++){
      var a=Math.random()*Math.PI*2,sp=0.5+Math.random()*3;
      stars.push({x:cx,y:cy,vx:Math.cos(a)*sp,vy:Math.sin(a)*sp,alpha:0.4+Math.random()*0.6,col:Math.random()>0.5?'#9999FF':'#ffffff'});
    }
    var t0=null,DUR=4200;
    function tick(ts){
      if(!t0)t0=ts;
      var el=ts-t0,prog=Math.min(el/DUR,1);
      var fade=prog<0.1?prog*8:prog>0.82?(1-prog)*5.5:0.94;
      ctx.fillStyle='rgba(0,0,0,'+fade+')';ctx.fillRect(0,0,W,H);
      var wp=Math.min(el/700,1);
      stars.forEach(function(s){
        s.x+=s.vx*(1+wp*20);s.y+=s.vy*(1+wp*20);
        var tl=1+wp*44;
        ctx.strokeStyle=s.col;ctx.globalAlpha=s.alpha*(prog>0.8?(1-prog)*5:1);
        ctx.lineWidth=1+wp*1.5;
        ctx.beginPath();ctx.moveTo(s.x,s.y);ctx.lineTo(s.x-s.vx*tl,s.y-s.vy*tl);ctx.stroke();
        ctx.globalAlpha=1;
        if(s.x<0||s.x>W||s.y<0||s.y>H){
          var a2=Math.random()*Math.PI*2,sp2=0.5+Math.random()*3;
          s.x=cx;s.y=cy;s.vx=Math.cos(a2)*sp2;s.vy=Math.sin(a2)*sp2;
        }
      });
      if(el>420)qEl.style.opacity='1';
      if(prog<1){requestAnimationFrame(tick);}
      else{canvas.remove();overlay.remove();warpActive=false;}
    }
    requestAnimationFrame(tick);
  }
})();
</script>

*EventLoop is live at [eventloop.city](https://eventloop.city) — source at [github.com/lorenanicole/event-loop](https://github.com/lorenanicole/event-loop). Python 3.15.0 final released 2026-10-09 — [announcement](https://blog.python.org/2026/10/python-3150-final-is-here), [download](https://python.org/downloads/release/python-3150/). All PEP numbers and feature descriptions reference the [official Python 3.15 What's New](https://docs.python.org/3.15/whatsnew/3.15.html). uv 0.12.24 is the current stable release as of this writing.*
