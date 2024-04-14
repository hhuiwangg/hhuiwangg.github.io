---
layout: page
title: MELP Level Set
img: assets/img/publication_preview/melp-levelset-preview.jpg
importance: 1
category: research
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/melp-levelset/representative.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

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
  .before,
  .after {
    margin: 0;
  }

  .before figcaption,
  .after figcaption {
    background: #fff;
    border: 1px solid #c0c0c0;
    border-radius: 12px;
    color: #2e3452;
    opacity: 0.8;
    padding: 12px;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    line-height: 100%;
  }

  .before figcaption {
    left: 12px;
  }

  .after figcaption {
    right: 12px;
  }
</style>

<img-comparison-slider hover="hover">
  <figure slot="first" class="before">
    <img width="100%" src="/assets/img/melp-levelset/double_bubble.render.0400.jpg">
    <figcaption>Render</figcaption>
  </figure>
  <figure slot="second" class="after">
    <img width="100%" src="/assets/img/melp-levelset/double_bubble.el.0400.jpg">
    <figcaption>Particle</figcaption>
  </figure>
</img-comparison-slider>
