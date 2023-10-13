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


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

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
