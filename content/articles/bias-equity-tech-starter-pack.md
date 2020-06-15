Title: Your Bias And Equity in Tech Reading Starter Pack
tags: inclusion, diversity, bias, technology, equity
Date: 2020-06-14 

Increasingly we use our biometric data to power the tech we use in our day to day lives. From using our face to unlock our smart phones to using <a href="https://www.clearme.com/how-it-works/">our fingerprints for air travel</a>, technology has enabled us to track and survey peoples at an alarming rate. Often in ways that are invisible to us and without our consent.

However, survelliance and its problematic relationship to technology is not new.
Since the launch of Amazon's facial recognition software - <a href="https://aws.amazon.com/rekognition/">Rekognition</a> - it has been subject to severe questioning. Especially as Amazon heavily targeted law enforcement as a client for Rekognition.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">ACLU took Amazon&#39;s facial recognition tech—which Amazon is aggressively selling to police—and loaded it with 25,000 mugshots. Then, they ran photos of members of Congress against the mugshots. <br><br>They got 28 matches, 40% of them Congressmen of color. <a href="https://t.co/Wix11Z3poY">https://t.co/Wix11Z3poY</a></p>&mdash; Trevor Timm (@trevortimm) <a href="https://twitter.com/trevortimm/status/1022498711157407745?ref_src=twsrc%5Etfw">July 26, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


In 2018, the ACLU raised several questions about the technology. One of the questions focused on how the system was built upon problematic data, namely a database of 25,000 public arrest photos. 

Datasets like mugshots <a href="https://www.cbsnews.com/news/facial-recognition-systems-racism-protests-police-bias/">are widely known to be biased</a> as they do not accurately reflect the makeup of the broader United States population. Specifically this data overrepresents BIPOC people. Also, the image quality of mugshots themselves are suspect and can often be of poor qaulity. 
Combined with other problems, like <a href="https://www.theguardian.com/technology/2018/jul/26/amazon-facial-rekognition-congress-mugshots-aclu">a higher false positive rate identifying BIPOC as offenders</a> and general problems of low accuracy the use of facial recognition in policing is again in the public limelight. The renewed focus on the Black Lives Matter movement and police brtuality has led to big tech companies like <a href="https://www.vox.com/recode/2020/6/10/21287194/amazon-microsoft-ibm-facial-recognition-moratorium-police">IBM, Amazon, and Microsoft stepping back - albeit temporarily - from selling facial recognition for law enforcement</a>. 
While facial recognition technology may be temporarily unavailable to law enforcement, there are several other questions we as technologists should be grappling with. The availability of a technology is only a part of the discussion,  the other problems to be discussed lies in the application of how this technology will be used. 

How facial recognition technology can be weaponized by policing, this will not be a uniform experience to all people. It will be informed by our social location - our race, our gender, our age, our area of residence. 

### Chicago: A Segregated City

Take Chicago as an example. Labeled at times the United State's most segregated city, this 2015 CMAP <a href="https://www.cmap.illinois.gov/updates/all/-/asset_publisher/UIMfSLnFfMB6/content/race-and-ethnicity-in-the-cmap-region">built with 2010 - 2014 American Community Survey data</a> shows us with data just how segregated the city it.

<div style="max-width: 400px, display: center">
    <img src="theme/images/cmap-2014.png" style="max-width: 100%, height:auto, width:auto, display: block">
</div>

The segregated landscape of Chicago is no accident. Instead we can understand Chicago as the result of decades, even centuries, of systemic racism and oppression.
One policy that clearly demonstrates the intentional remapping of Chicago's communities can be seen in <a href="https://www.wbez.org/stories/new-redlining-maps-show-chicago-housing-discrimination/37c0dce7-0562-474a-8e1c-50948219ecbb">redlining</a>. As a fiscal policy, redlining operated by labeling Chicago community areas on a scale from the "best" places for investment to the worst, or most "hazardous", places for investment. 

<div style="max-width: 400px, display: center">
    <img src="theme/images/redlining.jpg" style="max-width: 100%, height:auto, width:auto, display: block">
</div>

Throughout the 1930s and 1940s the federal Home Owners' Loan Corporation, backed by the Federal Housing Authority (FHA), used this practice of labeling communities of color - largely Black communities - overwhemlingly as red, or "hazardous". The "hazardous" labeling meant that in these areas loans were not extended. As these loans were backed by the FHA, <a href="https://www.theatlantic.com/magazine/archive/2014/06/the-case-for-reparations/361631/">the loans had a low interest rate and required a smaller down payment for purchasing a home</a>. Additionally these loans became the economic catalyst used by <a href="http://dspace.calstate.edu/bitstream/handle/10211.3/180032/Erika.EmeryDissertation.pdf?sequence=4">white America to finance their dreams of sending their children to college</a>. Redlining is but one example demonstrating how divestment, informed by race and other socioeconomic factors, had the intended result of moving wealth out of BIPOC communities. Wealth that, while moving out of BIPOC communities, was concentrated in white communities.

### My Chicago is not your Chicago

Systemic racism however is not only experienced in housing. Policing is intrinsically connected to housing as is wealth. Areas where police are deployed, or are not deployed, the way that policing happens; how one person experiences policing is greatly informed by the hyperlocal conditions on the ground as well as one's identity.

Some quick stats:

- <a href="https://www.thetrace.org/2016/12/murder-inequality-neighborhood-homicide-rates/">Chicago's South and West sides are the community areas with the highest homicide rates</a><
- <a href="https://chiyouthjustice.files.wordpress.com/2015/11/arresting-justice_facebook.jpg">Most of the arrests in a given year are BIPOC</a><
- Most police deployed in the highest crime Chicago community areas are <a href="https://www.themarshallproject.org/2016/09/20/the-most-dangerous-neighborhood-the-most-inexperienced-cops">also the most inexperienced</a>

Additionally, the areas hardest hit by COVID19 are <a href="https://abc7chicago.com/coronavirus-illinois-chicago-black-deaths/6203131/">overwhemingly BIPOC communities</a>.

<div style="max-width: 400px, display: center">
    <img src="theme/images/covid19-zip.png" style="max-width: 100%, height:auto, width:auto, display: block">
</div>

>> So why should we care about systems of oppression? 

When we as technologists build tools, we are not building technology in a vacuum. We do not build them devoid of the bias in the world around us. Nor do we fully have control over the way our tools will be employed.
It is our moral imperative to question not only how our technology is built, but why we need it. If the tools we create are based on the social landscape we live in, our tools merely "codigy the past". That is, we as technologists should not presume that our techology can, "invent the future" as author and activst <a href="https://weaponsofmathdestructionbook.com/">Cathy O'Neil warns us</a>. "Doing that requires moral imagination, and that's something only humans can provide".

I am calling on you all to take time to educate yourself and understand how technology intersects with bias, with systems of power, and systems of inequity.
I've started a bias and equity in technology reading list that I will be reading through as well as 
soliciting feedback on. 

<div style="max-width: 400px, display: center">
    <img src="theme/images/reading-list.JPG" style="max-width: 100%, height:auto, width:auto">
</div>

If you have a suggestion that should be added to the list you can add 👉 <a href="biasin.tech">here</a>.

We all have to do the work. To show up. To listen. To learn. To stay engaged. Will you join me?