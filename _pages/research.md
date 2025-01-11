---
permalink: /
title: "Gravitational Wave Astronomy"
permalink: /research/
author_profile: true
---
<head>
    <style>
        img {
            padding-right: 10px; 
        }
		
		blockquote  {
			font-size: 0.9em !important;
}
    </style>
	
</head>


<blockquote cite="https://eprints.soton.ac.uk/494760/">
"Shortly before 5AM local time on the 14th September 2015, a small disturbance was
noted at the LIGO facility in Livingston, Louisiana. The sophisticated instruments
contained within the site’s 4km long arms had detected changes in their length of barely
1 part per 10^21, around one thousandth of the width of a proton. On the other side
of the United States, Livingston’s sister facility at Hanford, Washington, detected the
same event 7ms later. Subsequent analysis would identify the origin of this disturbance
as the merger of two black holes, with masses approximately 36 and 29 times that of
the Sun, in a galaxy 1.3 billion light years away..." <i> from Chapter 1 of my <a href="https://eprints.soton.ac.uk/494760/">PhD thesis</a>.</i>
</blockquote>

The landmark first direct detection of gravitational waves by the LIGO and Virgo collaborations in 2015 opened a unique window into the population of binary black holes and neutron stars in our universe, and the strong gravitational fields that surround them. This achievement -- and the continued success of gravitational wave astronomy -- rely critically on our ability to accurately predict the gravitational wave emission from astrophysical sources. You can read about my efforts in this area below:

<head>
    <title>Gravitational self-force</title>
    <style>
        .collapsible {
            border: 1px solid #ccc;
            border-radius: 5px;
            margin: 10px 0;
            overflow: hidden;
        }

        .header {
            background-color: #f0f0f0;
            padding: 10px;
            cursor: pointer;
            font-weight: bold;
        }

        .content {
            display: none; /* Hidden by default */
            padding: 10px;
            background-color: #fff;
        }

        .content.visible {
            display: block; /* Show content when toggled */
        }
    </style>
</head>
<body>
    <div class="collapsible">
        <div class="header" onclick="toggleCollapsible(this)">
            Gravitational self-force and gravitational scattering
        </div>
        <div class="content">
            <p>Gravitational self-force (GSF) is an approach for modelling the general relativistic dynamics of binary systems where one object is significantly more massive than the other. The primary astrophysical application of GSF is in the modelling of intermediate and extreme mass-ratio inspirals, promising classes of observational targets for the planned space-based gravitational wave detector, LISA. </p>

			<p>In recent years, however, growing attention has also been paid to the problem of black hole <i>scattering</i>, where the two black holes interact but avoid merging and then move apart for ever after. Scattering events are less significant observational candidates compared to inspirals, but are excellent theoretical probes of the strong-field gravitational potential in the vicinity of black holes. Information about the universal gravitational interaction can be extracted from scattering simulations, and multiple pathways have been proposed through which GSF scatter calculations can improve our models of compact binary inspirals, even for <i>comparable mass</i> binaries such as those detected by LIGO and Virgo.</p>

			<p>My research in this area focuses on developing numerical methods to calculate the self-force experienced during scatter interactions. As part of my PhD research, I <a href="/publication/2023-05-16-2305-09724">investigated</a> the challenges faced when extending existing Fourier-domain techniques developed for bound-orbit self-force calculations to the scatter problem, and demonstrated how these could be overcome to enable a calculation of the self-force along scatter orbits in a scalar-field toy-model. I then applied this method as part of <a href="/publication/2024-06-13-2406-08363">work </a> that illustrated an approach to extend the range of validity of weak-field post-Minkowskian expansions by incorporating information from self-force calculations along strong-field scatter orbits. I continue to work towards a calculation of the gravitational self-force along scatter orbits.</p>

            
        </div>
    </div>

    <script>
        function toggleCollapsible(header) {
            const content = header.nextElementSibling;
            content.classList.toggle('visible');
        }
    </script>
</body>



<head>
    <title>Waveform acceleration</title>
    <style>
        .collapsible {
            border: 1px solid #ccc;
            border-radius: 5px;
            margin: 10px 0;
            overflow: hidden;
        }

        .header {
            background-color: #f0f0f0;
            padding: 10px;
            cursor: pointer;
            font-weight: bold;
        }

        .content {
            display: none; /* Hidden by default */
            padding: 10px;
            background-color: #fff;
        }

        .content.visible {
            display: block; /* Show content when toggled */
        }
    </style>
</head>
<body>
    <div class="collapsible">
        <div class="header" onclick="toggleCollapsible(this)">
            Waveform acceleration and surrogate modelling
        </div>
        <div class="content">
            <p>In order to identify gravitational wave events from detector data, and to accurately estimate the parameters of the source responsible, we may have to calculate the gravitational waveform for in excess of millions of different binary configurations. It is therefore essential that our waveform models are not only accurate, but also sufficiently fast to evaluate as and when required. One way to increase the speed of a waveform model is to build a <i>surrogate</i> which, when trained on a sufficiently large set of calibration waveforms, can accurately predict the output of the original waveform model for any set of input parameters. Crucially, the surrogate should be sufficiently fast to evaluate on demand during search/parameter estimation, while the original, typically much slower, waveform model is only needed to create the calibration data ahead of time.</p> 

			<p>My research focuses on creating surrogates for <i>effective-one-body</i> waveform models, with a particular emphasis on models that incorporate spin-precession. The challenge in this case is the high-dimensionality of the parameter space describing precessing binaries: 1 dimension for the mass-ratio of the system and 3 dimensions describing the spin of each of the two black holes, for a total of 7 dimensions. Interpolating waveform quantities across such a high-dimensional parameter space is challenging, and my work seeks to build off recent success using artificial neural networks for this task. </p>
           
        </div>
    </div>

    <script>
        function toggleCollapsible(header) {
            const content = header.nextElementSibling;
            content.classList.toggle('visible');
        }
    </script>
</body>
