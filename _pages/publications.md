---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<style>
  .row {
    display: flex;
    align-items: flex-start;       /* aligns first lines of text */
    border-bottom: 1px solid #aaa;  /* horizontal line below each row */
    padding-top: 0.1em;    /* slightly smaller */
	padding-bottom: 2.5em; /* slightly larger */
  }

  .column1 {
    width: 25%;
    padding: 5px;
  }

  .column2 {
    width: 75%;
    padding: 5px;
  }

  .column1 > *:first-child,
  .column2 > *:first-child {
    margin-top: 0;
  }

  .column1 p,
  .column2 p {
    margin: 0;
  }

  .column1 p + p,
  .column2 p + p {
    margin-top: 0.2em;
  }
  
	.image-container {
		padding-top:75px;
		padding-right: 15px;
		padding-bottom: 15px;
		padding-left: 15px;
	}
</style>


Details of my papers can also be found on [INSPIRE](https://inspirehep.net/authors/2750523?ui-citation-summary=true) and the [ADS](https://ui.adsabs.harvard.edu/search/q=author%3A%22Whittall%2C%20Christopher%22&sort=date%20desc%2C%20bibcode%20desc&p_=0).

{% include base_path %}

{% for post in site.publications reversed %}
<div class = "row">
	<div class="column1">
		<div class="image-container">
			<img src="{{post.illustration}}">
		</div>
	</div>
	
	<div class="column2">
		{% include archive-single.html %}
	</div>
</div>

{% endfor %}
