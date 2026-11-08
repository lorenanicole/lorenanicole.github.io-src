Title: Make It So: Election Night Was the Easy Part
Date: 2026-11-07 19:00
Category: Community
Tags: Community, Python, Civic Tech, Open Data, Star Trek
Slug: make-it-so-show-up-build-tools
Author: Lorena Mesa
Summary: Patrick Stewart is gone, and a wave of first-time leaders just got elected. Waves don't fail at the ballot box — they fail in the months after. Here's the arithmetic of the next election nobody is talking about, and a small Python tool for the work that comes after.

The first leader I ever wanted to be was bald, British and fictional.

Jean-Luc Picard.

I was a kid on a carpet in Illinois, blanket in my fists, and he made me believe I could lead something someday.

Five days before election night, [Patrick Stewart died at 86](https://chicago.suntimes.com/obituaries/2026/10/29/patrick-stewart-stage-giant-also-of-star-trek-and-x-men-fame-dies-at-86). He was my Captain.

Picard's gift wasn't being in charge. It was getting everyone on his bridge ready to be. He listened. He asked his officers what they thought, and he meant it. He trusted the people others overlooked. And when the talking was done, he made a decision and owned it.

<style>
/* "Make it so" as the beat it is. Deliberately dark in both themes -- it is a
   window, not a UI surface -- so the colors are painted explicitly, never inherited. */
.order {
  position: relative; overflow: hidden; isolation: isolate;
  margin: 2.75rem 0; padding: clamp(2rem, 7vw, 3.5rem) clamp(1rem, 4vw, 2rem);
  border-radius: 14px; text-align: center;
  background: radial-gradient(120% 140% at 18% 0%, #241b4a 0%, #120f2b 45%, #07060f 100%);
}
.order__sky, .order__sky::after {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
}
.order__sky { background-image:
    radial-gradient(1.4px 1.4px at 89% 80%, #fff, transparent),
    radial-gradient(1.3px 1.3px at 47% 54%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 88% 22%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 49% 92%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 80% 13%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 17% 89%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 50% 14%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 30% 80%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 17% 64%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 27% 38%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 28% 46%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 34% 45%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 22% 28%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 5% 71%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 7% 13%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 51% 87%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 20% 41%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 88% 86%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 80% 17%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 9% 86%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 52% 56%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 22% 73%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 47% 57%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 23% 48%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 51% 38%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 24% 38%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 24% 19%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 16% 73%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 70% 71%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 58% 84%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 11% 33%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 49% 87%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 75% 41%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 76% 8%, rgba(255,255,255,.9), transparent), radial-gradient(1.3px 1.3px at 65% 68%, rgba(255,255,255,.9), transparent);
}
.order__sky::after { background-image:
    radial-gradient(1px 1px at 6% 75%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 31% 79%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 77% 38%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 75% 12%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 40% 50%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 64% 19%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 44% 10%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 17% 83%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 67% 43%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 71% 72%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 77% 85%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 56% 14%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 31% 14%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 3% 31%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 87% 15%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 55% 36%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 96% 44%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 54% 68%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 35% 71%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 93% 54%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 51% 5%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 21% 53%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 11% 8%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 54% 40%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 76% 87%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 17% 61%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 11% 64%, rgba(255,255,255,.45), transparent), radial-gradient(1px 1px at 57% 22%, rgba(255,255,255,.45), transparent);
  animation: twinkle 4.5s ease-in-out infinite alternate;
}
@keyframes twinkle { from { opacity: .35 } to { opacity: 1 } }
.order__comet { position: absolute; top: 14%; left: -22%; width: 46%; height: auto;
                 z-index: -1; opacity: .9; animation: fly 9s ease-in-out infinite; }
@keyframes fly {
  0%   { transform: translate3d(0,0,0) rotate(0deg); opacity: 0 }
  12%  { opacity: .95 }
  55%  { opacity: .95 }
  75%  { transform: translate3d(230%, 165%, 0) rotate(0deg); opacity: 0 }
  100% { transform: translate3d(230%, 165%, 0); opacity: 0 }
}
.order__text {
  display: inline-block; color: #fff;
  font: 800 clamp(1.7rem, 7.5vw, 3.4rem)/1.05 ui-sans-serif, system-ui, sans-serif;
  letter-spacing: .14em; text-transform: uppercase; text-wrap: balance;
  text-shadow: 0 0 26px rgba(150,170,255,.65), 0 0 60px rgba(90,110,255,.35);
}
@media (prefers-reduced-motion: reduce) {
  .order__sky::after, .order__comet { animation: none }
  .order__comet { opacity: .9; transform: translate3d(140%, 90%, 0) }
}
</style>

<div class="order">
  <div class="order__sky" aria-hidden="true"></div>
  <svg class="order__comet" viewBox="0 0 220 60" aria-hidden="true" focusable="false">
    <defs><linearGradient id="comet1" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/>
      <stop offset="1" stop-color="#d6e4ff" stop-opacity=".95"/>
    </linearGradient></defs>
    <path d="M6 12 L188 43" stroke="url(#comet1)" stroke-width="3" stroke-linecap="round" fill="none"/>
    <circle cx="192" cy="44" r="11" fill="#fff" opacity=".22"/>
    <circle cx="192" cy="44" r="4.5" fill="#fff"/>
  </svg>
  <span class="order__text">Make it so.</span>
</div>

Stewart didn't only play that. As a boy he watched his father abuse his mother, and he spent the rest of his life working against it: as a patron of Refuge, the domestic violence charity, since 2007, for his mother, and with [Combat Stress](https://www.forbes.com/sites/marianneschnall/2026/11/02/remembering-patrick-stewarts-commitment-to-womens-rights-and-social-change/), the veterans' mental health charity, for his father, who came home from the war with shell shock, what we would now call PTSD. About his mother, [he said](https://predatorwatchwy.substack.com/p/his-mothers-name-how-patrick-stewart):

> I couldn't help her then. Now I can.

Not in a year when it trended. Not for a news cycle. For nearly twenty years.

That is the whole lesson, and it is the only one this post has.

I've been thinking about it this week, because on Tuesday a lot of new people were handed the conn.

## A wave of firsts

The 2026 midterms put people into high office who had, until now, mostly been kept at the edges. Across both parties, voters elected:

- **Deb Haaland** in New Mexico, the [first Native American woman elected governor](https://www.pbs.org/newshour/show/new-mexicos-deb-haaland-on-making-history-as-first-native-american-woman-elected-governor) of any U.S. state.
- **Keisha Lance Bottoms** in Georgia, the [first Black woman elected governor](https://www.npr.org/2026/11/03/g-s1-151040/georgia-elects-the-nations-first-black-female-governor) of any state.
- **Chris Pappas** of New Hampshire, the [first out gay man elected to the U.S. Senate](https://19thnews.org/2026/11/election-results-new-hampshire-senate/).
- **Julia Letlow** of Louisiana, the state's [first Republican woman elected to the Senate](https://www.wafb.com/2026/11/04/julia-letlow-projected-win-louisiana-senate-race/).
- **Gina Hinojosa**, [Texas's first Latina governor](https://www.kwtx.com/2026/11/04/gina-hinojosa-elected-texas-governor-becoming-first-latina-hold-office/).
- **Peggy Flanagan** of Minnesota, the [first Native American woman elected to the U.S. Senate](https://www.mprnews.org/story/2026/11/03/native-american-politician-peggy-flanagan-wins-minnesotas-open-us-senate-seat).
- **Abdul El-Sayed** of Michigan, the [first Muslim elected to the U.S. Senate](https://www.cbsnews.com/detroit/news/el-sayed-victory-speech-michigan-senate-first-muslim-senator/).
- **Melat Kiros** of Colorado, the [first Gen Z woman elected to Congress](https://www.npr.org/2026/11/03/g-s1-150229/melat-kiros-first-gen-z-woman-elected-to-congress), at 29.

The records are not only about who ran. At least [159 women will serve in the 120th Congress](https://cawp.rutgers.edu/blog/results-women-congressional-and-statewide-executive-candidates-election-2026), a new high, past the record of 152 set in 2024, and at least 136 in the House, 31.3% of it. Black women and Latinas both set new records for congressional representation. At least 17 women will be governors, 34% of the country's governorships, past [the old record of 14](https://cawp.rutgers.edu/news-media/press-releases/matching-and-sustaining-record-number-women-governors-new-record-number). Georgia, Minnesota, Ohio and Tennessee elected a woman governor for the first time. (A few races were still too close to call when I wrote this, so some of those counts may still move.)

Young people turned out too. CIRCLE at Tufts estimates [27% of young people voted, the second-highest midterm youth turnout in thirty years](https://circle.tufts.edu/2026-election), and about 30% in battleground states. It's an early estimate; CIRCLE will update it in spring 2027 once voter files are in.

That said, the trends do not all run one way. Women's representation in the Senate goes down next year, from 27 to at least 23. And fourteen states have still never had a woman governor at all.

While those are the numbers, what it felt like to me was a song.

I grew up dancing to "Bidi Bidi Bom Bom" after watching the *Selena* movie with my cousin Amy and my sister Erin, who — I will die on this hill — reminds me of and is *my* Selena. We watched it for the first time at my abuela's house.

On Tuesday night, [they played "Como la Flor"](https://www.instagram.com/reel/DfVyB58SXFZ/) at Gina Hinojosa's victory party.

I saw three people at once. The kid on the carpet. Me now. And whoever is small right now and is going to grow up with a Latina governor of Texas as the ordinary picture of what a governor looks like.

<div class="rose-wrap">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-50 -25 520 570"
     role="img" width="100%" style="display:block;max-width:340px;height:auto;margin:2rem auto" aria-labelledby="rose-title" xmlns:c2pa="http://c2pa.org/manifest"><metadata><c2pa:manifest>AAAWgmp1bWIAAAAeanVtZGMycGEAEQAQgAAAqgA4m3EDYzJwYQAAABZcanVtYgAAAEdqdW1kYzJtYQARABCAAACqADibcQN1cm46YzJwYTplZmZiZmIwZS1lODJlLTQ5YjEtOGVkMi1jYTdjYzFmYzhlMTcAAAADl2p1bWIAAAApanVtZGMyYXMAEQAQgAAAqgA4m3EDYzJwYS5hc3NlcnRpb25zAAAAALxqdW1iAAAARGp1bWRjYm9yABEAEIAAAKoAOJtxE2MycGEuaW5ncmVkaWVudC52MwAAAAAYYzJzaMg64NN6y05KE+8+n1hPbiwAAABwY2JvcqNpZGM6Zm9ybWF0bWltYWdlL3N2Zyt4bWxqaW5zdGFuY2VJRHgseG1wOmlpZDo3NTA3MjZjMC03ZWU5LTRiZWMtOWY3Ny0yOWY2ZjRiMzdjMThscmVsYXRpb25zaGlwaHBhcmVudE9mAAAB4mp1bWIAAABBanVtZGNib3IAEQAQgAAAqgA4m3ETYzJwYS5hY3Rpb25zLnYyAAAAABhjMnNoykXPMM6agj41DyIWQ4oxlQAAAZljYm9yomdhY3Rpb25zgqJmYWN0aW9ua2MycGEub3BlbmVkanBhcmFtZXRlcnOha2luZ3JlZGllbnRzgaJjdXJseC1zZWxmI2p1bWJmPWMycGEuYXNzZXJ0aW9ucy9jMnBhLmluZ3JlZGllbnQudjNkaGFzaFggJvvjD7/BGubLdquYVad30ScDk2iCIY5e8JAC2YtSyCWkZmFjdGlvbngdY29tLmFudGhyb3BpYy5jbGF1ZGUucHJvdmlkZWRqcGFyYW1ldGVyc6F4H2NvbS5hbnRocm9waWMub3JpZ2luLWNvbmZpZGVuY2VndW5rbm93bmtkZXNjcmlwdGlvbnhmQ2xhdWRlIHByb3ZpZGVkIHRoaXMgZmlsZSBhdCB0aGUgcmVxdWVzdCBvZiBhIHVzZXIgYW5kIG1heSBoYXZlIGNyZWF0ZWQgb3IgbW9kaWZpZWQgdGhlIGZpbGUgY29udGVudHMubXNvZnR3YXJlQWdlbnShZG5hbWVmQ2xhdWRlcmFsbEFjdGlvbnNJbmNsdWRlZPUAAADIanVtYgAAAEBqdW1kY2JvcgARABCAAACqADibcRNjMnBhLmhhc2guZGF0YQAAAAAYYzJzaE0i8TgoPgsgG5C75beTaJwAAACAY2JvcqVjYWxnZnNoYTI1NmNwYWRNAAAAAAAAAAAAAAAAAGRoYXNoWCDyc6AXG/l6KgyFl7Melz9RxOalU/dvt9Wu103adzlFgmRuYW1lbmp1bWJmIG1hbmlmZXN0amV4Y2x1c2lvbnOBomVzdGFydBj+Zmxlbmd0aBkeBAAAAj5qdW1iAAAAJ2p1bWRjMmNsABEAEIAAAKoAOJtxA2MycGEuY2xhaW0udjIAAAACD2Nib3KlY2FsZ2ZzaGEyNTZpc2lnbmF0dXJleE1zZWxmI2p1bWJmPS9jMnBhL3VybjpjMnBhOmVmZmJmYjBlLWU4MmUtNDliMS04ZWQyLWNhN2NjMWZjOGUxNy9jMnBhLnNpZ25hdHVyZWppbnN0YW5jZUlEeCx4bXA6aWlkOjNmMzkxZDMzLTVhNzYtNGMzMS1iMjQ5LTg1OWRiNDkxYjdlY3JjcmVhdGVkX2Fzc2VydGlvbnODomN1cmx4LXNlbGYjanVtYmY9YzJwYS5hc3NlcnRpb25zL2MycGEuaW5ncmVkaWVudC52M2RoYXNoWCAm++MPv8Ea5st2q5hVp3fRJwOTaIIhjl7wkALZi1LIJaJjdXJseCpzZWxmI2p1bWJmPWMycGEuYXNzZXJ0aW9ucy9jMnBhLmFjdGlvbnMudjJkaGFzaFggHz+4uynG+veUhYWJHTRKEcsBcW0yaxKAyZ3mxl7PlqGiY3VybHgpc2VsZiNqdW1iZj1jMnBhLmFzc2VydGlvbnMvYzJwYS5oYXNoLmRhdGFkaGFzaFgg3Dw1dLZIlXoWwvdONOHD0g0RtW9LgVNSWkPCKNfwmdh0Y2xhaW1fZ2VuZXJhdG9yX2luZm+jZG5hbWVvQW50aHJvcGljIEZpbGVzZ3ZlcnNpb25lMS4wLjBrc3BlY1ZlcnNpb25lMi40LjAAABA4anVtYgAAAChqdW1kYzJjcwARABCAAACqADibcQNjMnBhLnNpZ25hdHVyZQAAABAIY2JvctKEWQISogEmGCFZAgowggIGMIIBjaADAgECAhRA5aAK7sI50L64g/oGQgU9Z1UTADAKBggqhkjOPQQDAzBJMRcwFQYDVQQKEw5BbnRocm9waWMsIFBCQzEuMCwGA1UEAxMlQW50aHJvcGljIENvbnRlbnQgQ3JlZGVudGlhbHMgUm9vdCBDQTAeFw0yNjA4MDcxODQzNTZaFw0yODA4MDYxOTQzNTZaMEQxFzAVBgNVBAoTDkFudGhyb3BpYywgUEJDMSkwJwYDVQQDEyBBbnRocm9waWMgQ2xhdWRlIENvbnRlbnQgU2lnbmluZzBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABJh6CmvLUBgFFNU0vUKlOVtE6djd17L5SuwX0LemFisBM3dkd/3cyjxFA3Qo5S46fX0/ihY0VZ7mfb9KF703t5OjWDBWMA4GA1UdDwEB/wQEAwIHgDAVBgNVHSUEDjAMBgorBgEEAYPoXgIBMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgwFoAUzlHiBIFOZFsj+OPEz5o+nMHXXMIwCgYIKoZIzj0EAwMDZwAwZAIwMXMdFJ4BetLLVY7ORuE9noqbbAZOZn/aArXyTwFAZfKrPzxF2vPoJNf1+UCdg1XGAjBwX1zd9WGqYkqmL5SFqw1QySjr1zJfpJM9+1rdDwSPLMOPOjKuiXjoU/pUUeG9RwmhY3BhZFkNngAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPZYQAPen3Pe/2De6iQT9WmGYKJSLDXkOEjex2vgUtmV24imT8QF6dulSaocnWlmXfgPYw0zuE7jZaBDrJ8U4poZn5U=</c2pa:manifest></metadata>
<title id="rose-title">A red rose on a green stem with two leaves, tilted to one side, white sparkles twinkling around its petals.</title>
<defs>
  <radialGradient id="rose-back" cx="50%" cy="35%" r="70%">
    <stop offset="0" stop-color="#b3122b"/><stop offset="1" stop-color="#4a0310"/>
  </radialGradient>
  <linearGradient id="rose-cup" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#8e0a1f"/><stop offset=".45" stop-color="#d81b38"/>
    <stop offset="1" stop-color="#6d0516"/>
  </linearGradient>
  <linearGradient id="rose-flap" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#ff5c74"/><stop offset=".6" stop-color="#d0142f"/>
    <stop offset="1" stop-color="#7a0718"/>
  </linearGradient>
  <radialGradient id="rose-heart" cx="50%" cy="40%" r="60%">
    <stop offset="0" stop-color="#ff7a8c"/><stop offset=".7" stop-color="#c3112c"/>
    <stop offset="1" stop-color="#5c0412"/>
  </radialGradient>
  <linearGradient id="rose-stem" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#1c4d26"/><stop offset=".45" stop-color="#4fae63"/>
    <stop offset="1" stop-color="#173f1f"/>
  </linearGradient>
  <linearGradient id="rose-leaf" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#5cc172"/><stop offset="1" stop-color="#1d5a2a"/>
  </linearGradient>
  <radialGradient id="rose-halo" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="#ff8fa0" stop-opacity=".35"/>
    <stop offset="1" stop-color="#ff8fa0" stop-opacity="0"/>
  </radialGradient>
  <filter id="rose-glow" x="-100%" y="-100%" width="300%" height="300%">
    <feGaussianBlur stdDeviation="2.2" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<style>
  .rose-edge { stroke: #3d020b; stroke-width: 1.6; stroke-linejoin: round; }
  .rose-vein { fill: none; stroke: #3d020b; stroke-width: 1.4; stroke-linecap: round; opacity: .55; }
  .rose-shine { fill: none; stroke: #ffd3da; stroke-width: 2.4; stroke-linecap: round; opacity: .55; }
  .rose-spark { fill: #fff; animation: rose-twinkle 2.6s ease-in-out infinite; }
  .rose-dust { fill: #fff6f8; animation: rose-shimmer 3s ease-in-out infinite; }
  @keyframes rose-twinkle {
    0%, 100% { transform: scale(.25) rotate(0deg); opacity: .15; }
    50% { transform: scale(1) rotate(45deg); opacity: 1; }
  }
  @keyframes rose-shimmer { 0%, 100% { opacity: .1; } 50% { opacity: 1; } }
  @media (prefers-reduced-motion: reduce) {
    .rose-spark, .rose-dust { animation: none; opacity: .9; }
  }
</style>
<g transform="rotate(-16 200 270)">
<ellipse cx="200" cy="180" rx="190" ry="160" fill="url(#rose-halo)"/>
<!-- stem and leaves -->
<path d="M200,262 C196,330 214,400 206,505" fill="none" stroke="url(#rose-stem)" stroke-width="10" stroke-linecap="round"/>
<path d="M203,350 L226,336 L206,364 Z" fill="#2d7a3d"/>
<path d="M205,430 L182,418 L204,446 Z" fill="#2d7a3d"/>
<path d="M202,320 C170,300 120,305 104,332 C136,350 180,346 202,320 Z" fill="url(#rose-leaf)" stroke="#123a1a" stroke-width="1.4"/>
<path d="M202,320 C170,322 140,326 112,331" fill="none" stroke="#123a1a" stroke-width="1.2" opacity=".6"/>
<path d="M207,398 C238,372 290,374 306,400 C276,422 228,420 207,398 Z" fill="url(#rose-leaf)" stroke="#123a1a" stroke-width="1.4"/>
<path d="M207,398 C240,396 270,398 298,401" fill="none" stroke="#123a1a" stroke-width="1.2" opacity=".6"/>
<!-- back petals -->
<path class="rose-edge" fill="url(#rose-back)" d="M200,126 C140,66 62,96 72,172 C80,224 132,246 176,232 Z"/>
<path class="rose-edge" fill="url(#rose-back)" d="M200,126 C260,66 338,96 328,172 C320,224 268,246 224,232 Z"/>
<path class="rose-edge" fill="url(#rose-back)" d="M128,116 C138,48 262,48 272,116 C248,104 152,104 128,116 Z"/>
<!-- cup -->
<path class="rose-edge" fill="url(#rose-cup)" d="M104,158 C98,232 154,272 200,272 C246,272 302,232 296,158 C268,170 236,176 200,176 C164,176 132,170 104,158 Z"/>
<!-- opening and heart -->
<path class="rose-edge" fill="url(#rose-heart)" d="M122,152 C130,98 270,98 278,152 C256,186 144,186 122,152 Z"/>
<path class="rose-edge" fill="#a80f27" d="M150,148 C152,112 248,112 250,148 C234,166 166,166 150,148 Z"/>
<path class="rose-vein" d="M200,150 C182,148 174,132 190,122 C210,112 232,128 224,146 C214,166 172,162 168,140 C164,116 196,100 230,110"/>
<path class="rose-shine" d="M150,124 C170,104 222,100 246,116"/>
<!-- front flaps folding outward -->
<path class="rose-edge" fill="url(#rose-flap)" d="M104,158 C80,196 92,246 152,266 C130,236 124,200 138,174 Z"/>
<path class="rose-edge" fill="url(#rose-flap)" d="M296,158 C320,196 308,246 248,266 C270,236 276,200 262,174 Z"/>
<path class="rose-edge" fill="url(#rose-flap)" d="M128,186 C150,218 214,224 266,196 C262,238 230,266 196,266 C160,264 132,236 128,186 Z"/>
<path class="rose-vein" d="M150,214 C176,232 220,232 250,214"/>
<path class="rose-shine" d="M100,190 C100,214 112,236 134,250"/>
<path class="rose-shine" d="M150,236 C170,252 214,254 240,238"/>
<!-- sparkle -->
<g filter="url(#rose-glow)">
  <circle class="rose-dust" cx="188.0" cy="123.8" r="1.2" style="animation-delay:1.89s"/>
  <circle class="rose-dust" cx="144.7" cy="132.8" r="2.1" style="animation-delay:1.87s"/>
  <circle class="rose-dust" cx="162.9" cy="215.8" r="1.2" style="animation-delay:2.82s"/>
  <circle class="rose-dust" cx="127.2" cy="213.5" r="1.2" style="animation-delay:1.42s"/>
  <circle class="rose-dust" cx="251.6" cy="130.7" r="1.6" style="animation-delay:1.24s"/>
  <circle class="rose-dust" cx="87.5" cy="200.1" r="2.1" style="animation-delay:2.50s"/>
  <circle class="rose-dust" cx="190.6" cy="240.0" r="1.6" style="animation-delay:2.11s"/>
  <circle class="rose-dust" cx="166.9" cy="298.7" r="1.6" style="animation-delay:0.41s"/>
  <circle class="rose-dust" cx="276.1" cy="209.9" r="2.1" style="animation-delay:0.35s"/>
  <circle class="rose-dust" cx="167.6" cy="69.0" r="1.6" style="animation-delay:1.40s"/>
  <circle class="rose-dust" cx="167.7" cy="235.5" r="1.2" style="animation-delay:0.74s"/>
  <circle class="rose-dust" cx="269.4" cy="205.5" r="1.6" style="animation-delay:0.34s"/>
  <circle class="rose-dust" cx="163.2" cy="215.9" r="1.2" style="animation-delay:2.28s"/>
  <circle class="rose-dust" cx="164.8" cy="135.0" r="0.9" style="animation-delay:0.24s"/>
  <circle class="rose-dust" cx="231.6" cy="113.3" r="1.6" style="animation-delay:1.88s"/>
  <circle class="rose-dust" cx="287.0" cy="231.4" r="2.1" style="animation-delay:1.69s"/>
  <circle class="rose-dust" cx="126.7" cy="192.1" r="1.2" style="animation-delay:0.50s"/>
  <circle class="rose-dust" cx="139.3" cy="224.0" r="2.1" style="animation-delay:0.73s"/>
  <circle class="rose-dust" cx="169.3" cy="272.2" r="1.2" style="animation-delay:2.31s"/>
  <circle class="rose-dust" cx="293.0" cy="246.5" r="1.2" style="animation-delay:0.68s"/>
  <circle class="rose-dust" cx="272.8" cy="163.8" r="1.6" style="animation-delay:2.18s"/>
  <circle class="rose-dust" cx="256.7" cy="117.6" r="0.9" style="animation-delay:2.25s"/>
  <circle class="rose-dust" cx="145.1" cy="164.9" r="1.6" style="animation-delay:2.73s"/>
  <circle class="rose-dust" cx="223.0" cy="115.9" r="2.1" style="animation-delay:2.55s"/>
  <circle class="rose-dust" cx="180.7" cy="202.5" r="0.9" style="animation-delay:0.31s"/>
  <circle class="rose-dust" cx="298.6" cy="211.3" r="1.6" style="animation-delay:0.77s"/>
  <circle class="rose-dust" cx="232.2" cy="173.5" r="1.6" style="animation-delay:2.17s"/>
  <circle class="rose-dust" cx="280.8" cy="208.6" r="1.2" style="animation-delay:0.44s"/>
  <circle class="rose-dust" cx="223.6" cy="152.0" r="1.6" style="animation-delay:1.37s"/>
  <circle class="rose-dust" cx="267.8" cy="235.2" r="1.6" style="animation-delay:1.05s"/>
  <circle class="rose-dust" cx="180.3" cy="217.4" r="1.2" style="animation-delay:2.87s"/>
  <circle class="rose-dust" cx="166.8" cy="154.8" r="0.9" style="animation-delay:1.40s"/>
  <circle class="rose-dust" cx="196.9" cy="138.0" r="1.6" style="animation-delay:0.11s"/>
  <circle class="rose-dust" cx="184.7" cy="193.3" r="0.9" style="animation-delay:0.50s"/>
  <circle class="rose-dust" cx="208.2" cy="111.1" r="0.9" style="animation-delay:2.88s"/>
  <circle class="rose-dust" cx="116.2" cy="191.4" r="1.6" style="animation-delay:2.35s"/>
  <circle class="rose-dust" cx="249.0" cy="96.0" r="0.9" style="animation-delay:0.45s"/>
  <circle class="rose-dust" cx="323.3" cy="171.9" r="2.1" style="animation-delay:2.46s"/>
  <circle class="rose-dust" cx="132.0" cy="215.2" r="1.6" style="animation-delay:0.21s"/>
  <circle class="rose-dust" cx="155.8" cy="190.7" r="0.9" style="animation-delay:0.41s"/>
  <circle class="rose-dust" cx="264.1" cy="103.2" r="0.9" style="animation-delay:1.04s"/>
  <circle class="rose-dust" cx="53.4" cy="160.5" r="2.1" style="animation-delay:0.38s"/>
  <circle class="rose-dust" cx="186.0" cy="224.2" r="1.2" style="animation-delay:0.87s"/>
  <circle class="rose-dust" cx="202.2" cy="176.7" r="0.9" style="animation-delay:0.78s"/>
  <circle class="rose-dust" cx="265.0" cy="98.9" r="0.9" style="animation-delay:2.01s"/>
  <circle class="rose-dust" cx="199.4" cy="99.7" r="1.2" style="animation-delay:1.56s"/>
  <circle class="rose-dust" cx="214.7" cy="75.9" r="2.1" style="animation-delay:0.89s"/>
  <circle class="rose-dust" cx="220.3" cy="229.9" r="2.1" style="animation-delay:0.04s"/>
  <circle class="rose-dust" cx="219.1" cy="126.2" r="1.2" style="animation-delay:0.77s"/>
  <circle class="rose-dust" cx="252.4" cy="231.9" r="1.6" style="animation-delay:2.62s"/>
  <circle class="rose-dust" cx="188.1" cy="231.4" r="2.1" style="animation-delay:2.19s"/>
  <circle class="rose-dust" cx="239.2" cy="234.8" r="2.1" style="animation-delay:2.27s"/>
  <circle class="rose-dust" cx="264.9" cy="153.6" r="1.2" style="animation-delay:2.08s"/>
  <circle class="rose-dust" cx="83.2" cy="168.6" r="1.6" style="animation-delay:1.11s"/>
  <circle class="rose-dust" cx="133.1" cy="158.3" r="1.6" style="animation-delay:0.36s"/>
  <circle class="rose-dust" cx="303.4" cy="295.9" r="1.6" style="animation-delay:1.61s"/>
  <circle class="rose-dust" cx="139.7" cy="159.4" r="1.6" style="animation-delay:2.75s"/>
  <circle class="rose-dust" cx="201.4" cy="295.7" r="2.1" style="animation-delay:1.91s"/>
  <circle class="rose-dust" cx="216.3" cy="179.7" r="1.6" style="animation-delay:1.61s"/>
  <circle class="rose-dust" cx="186.7" cy="243.8" r="0.9" style="animation-delay:2.31s"/>
  <circle class="rose-dust" cx="246.1" cy="185.0" r="2.1" style="animation-delay:1.32s"/>
  <circle class="rose-dust" cx="167.5" cy="130.0" r="0.9" style="animation-delay:0.48s"/>
  <circle class="rose-dust" cx="100.6" cy="205.3" r="1.6" style="animation-delay:2.71s"/>
  <circle class="rose-dust" cx="132.8" cy="143.9" r="0.9" style="animation-delay:2.38s"/>
  <circle class="rose-dust" cx="141.7" cy="135.0" r="1.6" style="animation-delay:0.06s"/>
  <circle class="rose-dust" cx="269.3" cy="157.6" r="0.9" style="animation-delay:1.15s"/>
  <circle class="rose-dust" cx="237.1" cy="115.5" r="1.6" style="animation-delay:2.50s"/>
  <circle class="rose-dust" cx="160.6" cy="268.1" r="1.2" style="animation-delay:2.39s"/>
  <circle class="rose-dust" cx="183.9" cy="234.2" r="2.1" style="animation-delay:0.42s"/>
  <circle class="rose-dust" cx="205.1" cy="109.4" r="1.6" style="animation-delay:2.83s"/>
  <path class="rose-spark" d="M300.0,66.0 Q304.2,87.8 326.0,92.0 Q304.2,96.2 300.0,118.0 Q295.8,96.2 274.0,92.0 Q295.8,87.8 300.0,66.0 Z" style="animation-delay:0.0s;transform-origin:300px 92px"/>
  <path class="rose-spark" d="M112.0,102.0 Q114.9,117.1 130.0,120.0 Q114.9,122.9 112.0,138.0 Q109.1,122.9 94.0,120.0 Q109.1,117.1 112.0,102.0 Z" style="animation-delay:0.9s;transform-origin:112px 120px"/>
  <path class="rose-spark" d="M318.0,199.0 Q320.4,211.6 333.0,214.0 Q320.4,216.4 318.0,229.0 Q315.6,216.4 303.0,214.0 Q315.6,211.6 318.0,199.0 Z" style="animation-delay:1.7s;transform-origin:318px 214px"/>
  <path class="rose-spark" d="M92.0,214.0 Q95.5,232.5 114.0,236.0 Q95.5,239.5 92.0,258.0 Q88.5,239.5 70.0,236.0 Q88.5,232.5 92.0,214.0 Z" style="animation-delay:0.4s;transform-origin:92px 236px"/>
  <path class="rose-spark" d="M236.0,116.0 Q237.9,126.1 248.0,128.0 Q237.9,129.9 236.0,140.0 Q234.1,129.9 224.0,128.0 Q234.1,126.1 236.0,116.0 Z" style="animation-delay:1.2s;transform-origin:236px 128px"/>
  <path class="rose-spark" d="M164.0,166.0 Q165.6,174.4 174.0,176.0 Q165.6,177.6 164.0,186.0 Q162.4,177.6 154.0,176.0 Q162.4,174.4 164.0,166.0 Z" style="animation-delay:2.1s;transform-origin:164px 176px"/>
  <path class="rose-spark" d="M262.0,239.0 Q263.8,248.2 273.0,250.0 Q263.8,251.8 262.0,261.0 Q260.2,251.8 251.0,250.0 Q260.2,248.2 262.0,239.0 Z" style="animation-delay:0.7s;transform-origin:262px 250px"/>
  <path class="rose-spark" d="M150.0,316.0 Q152.2,327.8 164.0,330.0 Q152.2,332.2 150.0,344.0 Q147.8,332.2 136.0,330.0 Q147.8,327.8 150.0,316.0 Z" style="animation-delay:1.5s;transform-origin:150px 330px"/>
  <path class="rose-spark" d="M278.0,360.0 Q279.9,370.1 290.0,372.0 Q279.9,373.9 278.0,384.0 Q276.1,373.9 266.0,372.0 Q276.1,370.1 278.0,360.0 Z" style="animation-delay:2.4s;transform-origin:278px 372px"/>
  <path class="rose-spark" d="M208.0,46.0 Q210.6,59.4 224.0,62.0 Q210.6,64.6 208.0,78.0 Q205.4,64.6 192.0,62.0 Q205.4,59.4 208.0,46.0 Z" style="animation-delay:1.9s;transform-origin:208px 62px"/>
</g>
</g>
</svg>
</div>

This post isn't about who won. It's about what comes next, and about who is walking into rooms they — or the people they represent — may never have been in before.

Go ahead and dance. I did. The firsts are real, they took decades, and anyone who tells you not to celebrate them has never waited for one.

## And one of them is my aunt

Mary Mesa was [elected to the Lake County Board in District 17](https://www.lakecountyil.gov/4138/November-3-2026-General-Election), by about five points. She is one of the most inspiring leaders I know, and she just won a seat most people in her area probably couldn't name.

Nineteen people sit on that board. They approve the county budget and every financial matter that reaches county government, in a county that contains [219 separate taxing bodies](https://www.lakecountyil.gov/5023/About-Us) — municipalities, townships, school districts, park districts, libraries, fire districts. Courts and public safety run on what those nineteen vote for.

I can't name all of my own local representatives. But I can tell you who makes me want to be more involved. My Aunt Mary saw something and decided to do something about it.

That is the room this whole post is about.

## The question history will actually ask

Here's the part nobody puts on a victory banner: election day is one day. Representation is every day after it.

Someday someone will write the history of the 2026 midterms. The only open question is whether the last chapter is about the people who got elected — or the people who kept showing up.

Because waves don't fail at the ballot box. They fail in the months after, when everyone who turned out once decides the work is done.

I learned that the slow way, in open source. I ran for the Python Software Foundation's Board of Directors and got a seat right away, which was luck. The part that wasn't luck took years: reading bylaws, reviewing grants, hunting for funding, sending email across every time zone to volunteers who were all doing it after their day jobs, and thanking the community for feedback I did not always enjoy hearing — then trying to be better. Then rotating out so someone new could rotate in. Getting elected was the easy part.

PyLadies Chicago taught me the same lesson on a smaller scale. Saying "welcome" never kept a new organizer. What kept them was the rest of us showing up, month after month, until the room felt like theirs.

Scale that up and the clock only gets longer. In 2008, after she lost the nomination, Hillary Clinton [said](https://www.pbs.org/newshour/politics/politics-jan-june08-clinton_06-07) the highest, hardest glass ceiling had about 18 million cracks in it. It took eighteen more years for a Black woman to be elected governor of any state.

A first is not a finish. People hold a seat because the people who put them there stay in the room.

## Closer to home: 108 days

Chicago's next municipal election is **February 23, 2027**. As I write this, on November 7, that is 108 days away.

On that ballot: mayor, city clerk, city treasurer, [all fifty alderpersons](https://www.chicagoelections.gov/news/2027-municipal-and-aldermanic-election-candidate-filing-schedule-and-locations), and the Police District Councils in each of the city's 22 police districts. If nobody clears a majority, a runoff follows on April 6.

Now the arithmetic. In November 2024, Chicago turnout was [**67.94%**](https://cboeprod.blob.core.usgovcloudapi.net/prod/2024-11/Proclamation%20of%20Official%20Results%20-%20November%205,%202024.pdf). In the February 2023 municipal election — the one that picked every alderperson in the city — it was [**35.85%**](https://app.chicagoelections.gov/documents/general/Proclamation%20of%20Final%20Results%20for%20the%20February%2028,%202023%20Municipal%20Election.pdf).

The people who decide whether your street gets plowed, where a zoning variance lands, and what your ward does with its menu money are chosen by barely half the crowd that shows up to pick a president.

<figure>
<img src="{static}/images/make-it-so-turnout-gap.svg"
     alt="Line chart of Chicago voter turnout, 1983 to 2024. Presidential general election turnout stays between 63 and 78 percent for the whole period, ending at 67.94 percent in November 2024. Chicago municipal turnout starts at 82.07 percent in April 1983, drops below 46 percent by 1991, and has sat between 33 and 42 percent ever since, ending at 35.85 percent in February 2023.">
<figcaption>Chicago turnout, 1983&ndash;2024. The solid line is the presidential general; the dashed line is the city&rsquo;s own municipal election. Source: Chicago Board of Election Commissioners, <em>Percentage of Voters Casting Ballots at Elections (1942&ndash;Present)</em>, plus the Board&rsquo;s result proclamations for 2023 and 2024. Municipal elections through 1995 were partisan and held in April; from 1999 they are nonpartisan and held in February, so the two halves of that line are not perfectly like for like.</figcaption>
</figure>

<details>
<summary>The same numbers as a table</summary>

<table>
  <thead>
    <tr><th scope="col">Year</th><th scope="col">Presidential general</th><th scope="col">Year</th><th scope="col">Chicago municipal</th></tr>
  </thead>
  <tbody>
    <tr><td>1984</td><td>78.23%</td><td>1983</td><td>82.07%</td></tr>
    <tr><td>1988</td><td>71.58%</td><td>1987</td><td>74.08%</td></tr>
    <tr><td>1992</td><td>74.57%</td><td>1991</td><td>45.06%</td></tr>
    <tr><td>1996</td><td>63.17%</td><td>1995</td><td>42.25%</td></tr>
    <tr><td>2000</td><td>70.22%</td><td>1999</td><td>41.92%</td></tr>
    <tr><td>2004</td><td>75.13%</td><td>2003</td><td>33.71%</td></tr>
    <tr><td>2008</td><td>73.87%</td><td>2007</td><td>33.08%</td></tr>
    <tr><td>2012</td><td>75.41%</td><td>2011</td><td>42.30%</td></tr>
    <tr><td>2016</td><td>71.04%</td><td>2015</td><td>34.03%</td></tr>
    <tr><td>2020</td><td>73.28%</td><td>2019</td><td>35.45%</td></tr>
    <tr><td>2024</td><td>67.94%</td><td>2023</td><td>35.85%</td></tr>
  </tbody>
</table>

</details>

Chicago is not a city that cannot be bothered. In April 1983 a municipal election here drew **82.07%** — higher than any presidential general in this chart. The ceiling is not the problem. The habit is.

This is not a Chicago quirk. It's the design. Sarah Anzia's [*Timing and Turnout*](https://press.uchicago.edu/ucp/books/book/chicago/T/bo16956602.html) (University of Chicago Press, 2014) found that off-cycle elections don't lower everyone's turnout equally — they lower it among people with no particular stake, while organized groups keep voting. The smaller the electorate, the larger the share those groups represent. The Public Policy Institute of California puts the gap at [roughly 36 percentage points](https://www.ppic.org/wp-content/uploads/content/pubs/report/R_302ZHR.pdf) between off-cycle city elections and those held alongside a presidential race.

Low turnout isn't apathy. It's a room with the lights dimmed, and somebody already sitting in it.

## Tuesday proved it cuts both ways

Here's the hopeful part, and it happened on the same ballot as the firsts.

Keisha Lance Bottoms said it on election night, after an opponent who had spent [nearly $200 million of his own money](https://fortune.com/2026/10/24/georgia-billionaire-gop-gubernatorial-candidate-rick-jackson-fortune-gods-money-200-million-campaign/) trying to beat her. [In her words](https://thegrio.com/2026/11/04/im-standing-on-shoulders-made-of-steel-keisha-lance-bottoms-delivers-powerful-victory-speech-after-historic-georgia-win/):

> You've shown that no amount of money will ever never ever ever overcome the power of the people.

She was talking about her own campaign. It was true somewhere much smaller on the same night.

Ballotpedia counted [41 local data center measures on the November 3 ballot across ten states](https://ballotpedia.org/Data_center-related_ballot_measures,_2026). Ohio alone had 21, across 18 jurisdictions. In Sunbury, residents passed a charter amendment restricting data centers drawing 25 megawatts or more. In Wilmington, [about 80% of voters rejected all four rezoning referendums](https://ballotpedia.org/Data_center-related_ballot_measures,_2026) that would have rezoned rural residential land for industrial use.

These were township zoning questions and charter amendments — the least-covered rooms in American government. And they just became the place where the largest infrastructure buildout of our lifetime gets decided.

I want to be careful here, because I write about AI and I build with it. This isn't a story about technology losing. It's a story about who gets a vote on where it goes, and what it costs them. Those are the rooms where that gets settled, and for one Tuesday, people filled them.

*(These counts were unofficial at the time of writing; I'll update them once they're certified.)*

## The Duty Roster

So I built the smallest possible thing that helps.

It's a roster: every election between now and 2028, plus the rooms that meet without a ballot — Police District Council meetings, Local School Council meetings, your ward office, Chi Hack Night. Each row lists when it happens, what it governs, the turnout the last comparable election drew, and where every one of those facts came from.

Each row has a button that says **Make it so**. It downloads a calendar file. Where a schedule belongs to your district, school or ward, the button says **Find yours** and goes to the official page instead.

That's the whole product. No account, no server, no API key. A pledge decays; a calendar entry goes off on February 23 whether or not you still feel like it.

I didn't copy the election dates from anywhere. The Illinois Election Code sets them by rule, so the code computes them from the law and checks them against the State Board of Elections' published calendar:

```python
import calendar
from datetime import date, timedelta

TUESDAY = calendar.TUESDAY


def last_weekday(year: int, month: int, weekday: int) -> date:
    last = date(year, month, calendar.monthrange(year, month)[1])
    return last - timedelta(days=(last.weekday() - weekday) % 7)


def consolidated_primary(year: int) -> date:
    """10 ILCS 5/2A-1.1: odd years, the last Tuesday in February.
    Chicago's mayor, clerk, treasurer and all 50 alderpersons are elected that day."""
    return last_weekday(year, 2, TUESDAY)


assert consolidated_primary(2023) == date(2023, 2, 28)  # the last one, per the election board
assert consolidated_primary(2027) == date(2027, 2, 23)  # the next one, per the State Board
# full implementation, with tests and every source: github.com/lorenanicole/blog-code/tree/main/make-it-so-show-up-build-tools
```

The calendar files follow the iCalendar standard (RFC 5545) to the letter, commas escaped and all, so any standards-following calendar app can open them. Each one is about a dozen lines of plain text. A dozen lines is the difference between remembering and forgetting.

Every number on the roster carries its source: turnout from the Chicago Board of Election Commissioners' official proclamations, meeting schedules from the City, CPS and the organizers themselves. A small script re-reads those pages to make sure the facts still hold. It asks each site's robots.txt for permission first, identifies itself, waits between requests, and touches nothing but public pages. No personal data goes in or comes out.

Meanwhile, YouTube keeps serving me ads for dollar stores, Starlink and how to ride the CTA. The unsettling part is that it's mostly right. I do shop the dollar store, and I always need help with the CTA. It knows because it watches. The roster doesn't, and won't.

**[Open the Duty Roster](/extra/roster/)**: five ballots and four rooms, each one sourced.

Not a code person? [Download the roster as a PDF](/extra/roster/duty-roster.pdf) to print, stick on the fridge, or forward to your group chat. Every link and date is in it.

## Engage

Picard didn't end a briefing with a speech. He ended it with one word.

Senator-elect Abdul El-Sayed ended his victory speech Tuesday night with six: "So Michigan, let's go build it."

Same beat. The talking is done, and the work starts now.

So here's my ask. Pick your post:

<style>
.posts { list-style: none; padding-left: 0; }
.posts li { position: relative; padding-left: 2rem; margin-bottom: .9rem; }
.posts .pip { position: absolute; left: 0; top: .3em; width: 1.1rem; height: 1.1rem;
              border-radius: 999px; border: 1.5px solid rgba(140,140,140,.5); }
.pip--gold { background: #d8a01a; }
.pip--blue { background: #2f6fd0; }
.pip--red  { background: #b7332a; }
</style>

<ul class="posts">
  <li><span class="pip pip--gold" aria-hidden="true"></span>
    <strong>Gold, operations.</strong> One project. Chi Hack Night has been building civic tech in Chicago for years. Bring a laptop.</li>
  <li><span class="pip pip--blue" aria-hidden="true"></span>
    <strong>Blue, sciences.</strong> One person. Mentor someone new, especially someone who's the first in their family, their team or their office to do the thing.</li>
  <li><span class="pip pip--red" aria-hidden="true"></span>
    <strong>Red, command.</strong> One meeting. A ward night, a school council, a police district council. Show up when there's no ballot on the table.</li>
</ul>

Then put the next one on your calendar before you close this tab. That's the only part that compounds.

The firsts got elected. Whether they get to govern is a question about day 108, and the runoff in April, and every quiet meeting in between.

<div class="engage-wrap">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300"
     role="img" width="100%" style="display:block;max-width:760px;height:auto;margin:2rem auto"
     aria-label="The word ENGAGE in wide squared science-fiction lettering, arched and filled
     with a rainbow gradient in the style of 1990s WordArt, on a black panel with starbursts.">
<defs>
  <linearGradient id="engage-rainbow" x1="90" y1="0" x2="670" y2="0" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#ff2d2d"/><stop offset=".18" stop-color="#ff8a00"/>
    <stop offset=".36" stop-color="#ffe600"/><stop offset=".54" stop-color="#31d843"/>
    <stop offset=".72" stop-color="#1f8bff"/><stop offset=".88" stop-color="#7b3dff"/>
    <stop offset="1" stop-color="#ff3dc4"/>
  </linearGradient>
  <linearGradient id="engage-panelbg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1b1b24"/><stop offset="1" stop-color="#05050a"/>
  </linearGradient>
</defs>
<style>
  .engage-fill path { stroke: #000; stroke-width: 7; paint-order: stroke;
                stroke-linejoin: round; }
  .engage-shadow path { fill: #000; opacity: .8; }
  .engage-spark { fill: #fff; }
</style>
<rect x="0" y="0" width="760" height="300" rx="18" fill="url(#engage-panelbg)"/>
<rect x="10" y="10" width="740" height="280" rx="12"
      fill="none" stroke="url(#engage-rainbow)" stroke-width="3"/>
<g transform="translate(7,7)">
<g class="engage-shadow">
  <path d="M0,0 H96 V21 H22 V50 H76 V70 H22 V99 H96 V120 H0 Z" transform="translate(160.52,209.59) rotate(-21.46) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd"/>
  <path d="M0,0 H24 L72,74 V0 H96 V120 H72 L24,46 V120 H0 Z" transform="translate(246.31,183.08) rotate(-12.87) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd"/>
  <path d="M96,0 H0 V120 H96 V54 H52 V75 H74 V99 H22 V21 H96 Z" transform="translate(335.10,169.68) rotate(-4.29) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd"/>
  <path d="M28,0 H68 L96,120 H72 L66,95 H30 L24,120 H0 Z M38,70 H58 L48,26 Z" transform="translate(424.90,169.68) rotate(4.29) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd"/>
  <path d="M96,0 H0 V120 H96 V54 H52 V75 H74 V99 H22 V21 H96 Z" transform="translate(513.69,183.08) rotate(12.87) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd"/>
  <path d="M0,0 H96 V21 H22 V50 H76 V70 H22 V99 H96 V120 H0 Z" transform="translate(599.48,209.59) rotate(21.46) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd"/>
</g>
</g>
<g class="engage-fill">
  <path d="M0,0 H96 V21 H22 V50 H76 V70 H22 V99 H96 V120 H0 Z" transform="translate(160.52,209.59) rotate(-21.46) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd" fill="#ff2d2d"/>
  <path d="M0,0 H24 L72,74 V0 H96 V120 H72 L24,46 V120 H0 Z" transform="translate(246.31,183.08) rotate(-12.87) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd" fill="#ff9400"/>
  <path d="M96,0 H0 V120 H96 V54 H52 V75 H74 V99 H22 V21 H96 Z" transform="translate(335.10,169.68) rotate(-4.29) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd" fill="#d1e30f"/>
  <path d="M28,0 H68 L96,120 H72 L66,95 H30 L24,120 H0 Z M38,70 H58 L48,26 Z" transform="translate(424.90,169.68) rotate(4.29) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd" fill="#2bbe82"/>
  <path d="M96,0 H0 V120 H96 V54 H52 V75 H74 V99 H22 V21 H96 Z" transform="translate(513.69,183.08) rotate(12.87) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd" fill="#4d64ff"/>
  <path d="M0,0 H96 V21 H22 V50 H76 V70 H22 V99 H96 V120 H0 Z" transform="translate(599.48,209.59) rotate(21.46) scale(0.78) translate(-48.0,-120.0)" fill-rule="evenodd" fill="#ff3dc4"/>
</g>
<rect x="200" y="244" width="360" height="7" rx="3.5" fill="url(#engage-rainbow)"/>
  <path class="engage-spark" d="M74.0,70.0 Q77.7,88.3 96.0,92.0 Q77.7,95.7 74.0,114.0 Q70.3,95.7 52.0,92.0 Q70.3,88.3 74.0,70.0 Z"/>
  <path class="engage-spark" d="M686.0,61.0 Q689.2,76.8 705.0,80.0 Q689.2,83.2 686.0,99.0 Q682.8,83.2 667.0,80.0 Q682.8,76.8 686.0,61.0 Z"/>
  <path class="engage-spark" d="M108.0,218.0 Q110.4,229.6 122.0,232.0 Q110.4,234.4 108.0,246.0 Q105.6,234.4 94.0,232.0 Q105.6,229.6 108.0,218.0 Z"/>
  <path class="engage-spark" d="M652.0,210.0 Q654.7,223.3 668.0,226.0 Q654.7,228.7 652.0,242.0 Q649.3,228.7 636.0,226.0 Q649.3,223.3 652.0,210.0 Z"/>
</svg>
</div>

Until next time: live long, Python & prosper. 🖖
