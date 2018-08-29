Title: Building a GitHub page with Pelican, a Python static site generator
tags: pelican, python, github-page
Date: 2018-08-28 

If you've ever wanted to quickly spin up a personal website but, like me, are either preoccupied with design or want something basic to help you get started look no further. Static site generators are a great way to help you build a website if:

- you want to use a predefined css/html template
- don't want to deal with a complicated dynamic CMS like Wordpress
- want a page that will be served up fast!
- _are looking to add version control to your content_

The code behind my website is powered by [Pelican](http://docs.getpelican.com/), a Python static website generator. If you are curious about other static website generators, there are various [lists](https://www.creativebloq.com/features/10-best-static-site-generators) on the web that you can easily find with a Google search.

### How do I build a website with Pelican?

Below, I'll cover how to build a GitHub page website with Pelican that is hosted on (surprise surprise) GitHub. Additionally we'll review how to add version control to your GitHub repo that maintains the website content, the website theme, and Pelican code in separate repos. Lastly, we'll deploy the code to the GitHub page and even customize the GitHub page with a domain name.

### Getting started

You'll likely want to clone a copy [my repo](https://github.com/lorenanicole/lorenanicole.github.io-src) to follow along with the code snippets in this post. 

To download the code to your machine:

```bash
git clone --recursive repo-url  # downloads the submodules
```

### What's in the repo?

- Master (`lorenanicole.github.io-src`) repo
- `/output` dir points to [my GitHub pages repo](https://github.com/lorenanicole/lorenannicole.github.io) where Pelican builds and stores generated static files.
- '/voce' dir points to [fork of the Pelican theme voce](https://github.com/lorenanicole/voce) used in my website

To find more Pelican themes explore [here](http://www.pelicanthemes.com/).

Need help configuring your own Pelican repos? Read [here](https://fedoramagazine.org/make-github-pages-blog-with-pelican/). 

### Generating content

The Pelican theme (in this case `voce`) has templates that define the design of the website. The customizations for configuring a Pelican website are found in the `pelicanconf.py` file in this repo.

To create content add a Markdown or RST file with the name of the page or article you'd like to create. Markdown, as used in this repo, will need to be installed via `pip install Markdown`.

To write an article create a `.md` or `.rst` file in the `/content/articles` directory. You'll need to specify a title at a minimum, other attributes can be found here.

To write a page, again create create a `.md` or `.rst` file, this time in the `/content/pages` directory. Again you need to specify minimum metadata.

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

### How do you add your own domain to your github page?

You need to add a `CNAME` file with your domain name in your github pages repo. Additionally you'll need to configure your DNS record on your domain provider.

Examples tutorials:
- [Gandi + GitHub Pages](http://spector.io/how-to-set-up-github-pages-with-a-custom-domain-on-gandi/)
- [GoDaddy + GitHub Pages](https://medium.com/@supriyakankure/how-to-add-a-custom-domain-to-your-github-page-with-godaddy-84495781143e)

### Questions?

Please reach out! All my contact info is in the menu above. 