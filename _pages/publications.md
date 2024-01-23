---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<style>
    /* Define the styles for the columns */
    .column1 {
        float: left;
        width: 25%; 
     }
    .column2 {
        float: left;
        width: 75%; 
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
<div>
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
