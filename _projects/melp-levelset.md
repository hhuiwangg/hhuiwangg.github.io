---
layout: page
title: A Moving Least-Squares/Level-Set Particle Method for Bubble and Foam Simulation
description: A novel particle-grid scheme for simulating intricate bubble and foam flow, with MLS particles serving as interfacial trackers and surfacial discretization, enables solving both volumetric air-liquid flow and surface surfactant flow simultaneously
img: assets/img/publication_preview/melp-levelset-preview.jpg
importance: 1
category: research
related_publications: wang2024moving
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/melp-levelset/representative.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<br>

### Abstract
----

We present a novel particle-grid scheme for simulating bubble and foam flow. At the core of our approach lies a particle representation that combines the computational nature of moving least-squares particles and particle level-set methods. Specifically, we assign a dedicated particle system to each individual bubble, enabling accurate tracking of its interface evolution and topological changes in a foaming fluid system. The particles within each bubble's particle system serve dual purposes. Firstly, they function as a surface discretization, allowing for the solution of surfactant flow physics on the bubble's membrane. Additionally, these particles act as interface trackers, facilitating the evolution of the bubble's shape and topology within the multiphase fluid domain. The combination of particle systems from all bubbles contributes to the generation of an unsigned level-set field, further enhancing the simulation of coupled multiphase flow dynamics. By seamlessly integrating our particle representation into a multiphase, volumetric flow solver, our method enables the simulation of a broad range of intricate bubble and foam phenomena. These phenomena exhibit highly dynamic and complex structural evolution, as well as interfacial flow details.

<br>

<script
  defer
  src="https://cdn.jsdelivr.net/npm/img-comparison-slider@8/dist/index.js"
></script>
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/img-comparison-slider@8/dist/styles.css"
/>

<style>
    .before{
        margin: 0;
    }

    .after {
        margin: 0;
    }

    .before figcaption {
        background: #121212;
        border-radius: 0.2rem;
        color: #ffffff;
        opacity: 0.9;
        padding: 2px 10px;
        margin: 1rem;
        font-size: 1em;
        position: absolute;
        left: 0;
        bottom: 0;
        line-height: normal;
    }

    .after figcaption {
        background: #121212;
        border-radius: 0.2rem;
        color: #ffffff;
        opacity: 0.9;
        padding: 2px 10px;
        margin: 1rem;
        font-size: 1em;
        position: absolute;
        right: 0;
        bottom: 0;
        line-height: normal;
    }
</style>

### Results
----

#### Jet on bubbles | Double bubbles

<img-comparison-slider  style="width: 49%" hover="hover">
  <figure slot="first" class="before">
    <img width="100%" src="/assets/img/melp-levelset/water_on_bubble.rendered_seq.0100.jpg">
    <figcaption>Render</figcaption>
  </figure>
  <figure slot="second" class="after">
    <img width="100%" src="/assets/img/melp-levelset/water_on_bubble_mesh_particle.mantra1.0400.jpg">
    <figcaption>Mesh</figcaption>
  </figure>
</img-comparison-slider>

<img-comparison-slider  style="width: 49%" hover="hover">
  <figure slot="first" class="before">
    <img width="100%" src="/assets/img/melp-levelset/double_bubble.render.0400.jpg">
    <figcaption>Render</figcaption>
  </figure>
  <figure slot="second" class="after">
    <img width="100%" src="/assets/img/melp-levelset/double_bubble.el.0400.jpg">
    <figcaption>Particle</figcaption>
  </figure>
</img-comparison-slider>

<br>

#### Bubble life | Multi-bubbles on water

<img-comparison-slider  style="width: 49%" hover="hover">
  <figure slot="first" class="before">
    <img width="100%" src="/assets/img/melp-levelset/bubble_life.render.0180.jpg">
    <figcaption>Render</figcaption>
  </figure>
  <figure slot="second" class="after">
    <img width="100%" src="/assets/img/melp-levelset/bubble_life.particle.0180.jpg">
    <figcaption>Particle</figcaption>
  </figure>
</img-comparison-slider>

<img-comparison-slider  style="width: 49%" hover="hover">
  <figure slot="first" class="before">
    <img width="100%" src="/assets/img/melp-levelset/in_and_out.render.0250.jpg">
    <figcaption>Render</figcaption>
  </figure>
  <figure slot="second" class="after">
    <img width="100%" src="/assets/img/melp-levelset/in_and_out.el.0250.jpg">
    <figcaption>Particle</figcaption>
  </figure>
</img-comparison-slider>

<br>

#### Four bubbles | Rising bubbles

<img-comparison-slider  style="width: 49%" hover="hover">
  <figure slot="first" class="before">
    <img width="100%" src="/assets/img/melp-levelset/four_bubbles.render.0500.jpg">
    <figcaption>Render</figcaption>
  </figure>
  <figure slot="second" class="after">
    <img width="100%" src="/assets/img/melp-levelset/four_bubbles.particle.0500.jpg">
    <figcaption>Particle</figcaption>
  </figure>
</img-comparison-slider>

<img-comparison-slider  style="width: 49%" hover="hover">
  <figure slot="first" class="before">
    <img width="100%" src="/assets/img/melp-levelset/bubble_arise.render.0120.jpg">
    <figcaption>Render</figcaption>
  </figure>
  <figure slot="second" class="after">
    <img width="100%" src="/assets/img/melp-levelset/bubble_arise.mesh.0120.jpg">
    <figcaption>Mesh</figcaption>
  </figure>
</img-comparison-slider>

<br>
<br>

### Video
----
<div class="embed-responsive embed-responsive-16by9">
  <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/1tWclARBiHY" allowfullscreen></iframe>
</div>

<br>
<br>

### Links
----
[[Youtube]](https://www.youtube.com/watch?v=1tWclARBiHY)
[[Preprint]](/assets/pdf/mlsls_main.pdf)
[[Preprint (Compressed)]](/assets/pdf/mlsls_compressed.pdf)
[[Preprint (Appendix)]](/assets/pdf/mlsls_app.pdf)

<br>
<br>