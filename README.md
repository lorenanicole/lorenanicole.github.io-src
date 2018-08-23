# lorenanicole.github.io-src

This is the master repository that generates the content for [my personal website](http://lorenamesa.com). The code behind my website is powered by Pelican, a Python static website generator. 

## Getting started

```bash
git clone --recursive repo-url  # downloads the submodules
```

### What's in the repo?

- Master (this) repo
- `/output` dir points to [my GitHub pages repo](https://github.com/lorenanicole/lorenannicole.github.io) where Pelican builds and stores generated static files.
- '/voce' dir points to [fork of the Pelican theme voce](https://github.com/lorenanicole/voce) used in my website

To find more Pelican themes explore [here](http://www.pelicanthemes.com/).

Need help configuring your own Pelican repos? Read [here](https://fedoramagazine.org/make-github-pages-blog-with-pelican/). 

### Generating content

The Pelican theme (in this case voce) has templates that define the design of the website. The customizations for configuring a Pelican website are found in the `pelicanconf.py` file in this repo.

To create content add a Markdown or RST file with the name of the page or article you'd like to create. Markdown, as used in this repo, will need to be installed via `pip install Markdown`.

Once your pages (the site navigation sections defined in the menu) or articles (e.g. blog posts) are created you:

```bash
make html && make serve  # Exports static pages/articles to /output and serves locally
```

If all looks good you can: `make publish` (or `make html` but ensure your `SITE_URL` is set to not to `localhost` in `pelicanconf.py`).

```bash
cd /output
git remote -v  # ensure points to the github page repo
git add 
git commit -m 'new pages'
git push
```

Navigate to `yourusername.github.io` to see the changes real time!

For an entire overview of getting started with Pelican read the [documentation](http://docs.getpelican.com/en/3.1.1/getting_started.html).
### Questions or comments?

### How do you add your own domain to your github page?

You need to add a `CNAME` file with your domain name in your github pages repo. Additionally you'll need to configure your DNS record on your domain provider.

Examples tutorials:
- [Gandi + GitHub Pages](http://spector.io/how-to-set-up-github-pages-with-a-custom-domain-on-gandi/)
- [GoDaddy + GitHub Pages](https://medium.com/@supriyakankure/how-to-add-a-custom-domain-to-your-github-page-with-godaddy-84495781143e)

### Questions?

Navigate to [my website](http://lorenamesa.com) and find the contact info!
