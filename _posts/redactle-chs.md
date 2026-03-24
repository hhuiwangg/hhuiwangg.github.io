---
layout: distill
title: "Redactle-CHS: 汉字猜词挑战"
description: "自动化语言解谜游戏。"
tags: misc
giscus_comments: true
date: 2026-03-24
featured: true

authors:
  - name: Your Name
    url: "你的个人主页链接"
    affiliations:
      name: SJTU (上海交通大学)

# 如果你有参考文献可以保留，没有则删除
# bibliography: 2018-12-22-distill.bib

toc:
  - name: 游戏入口
  - name: 技术架构
  - name: 玩法说明

_styles: >
  .game-container {
    margin-top: 20px;
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    border-radius: 8px;
    overflow: hidden;
    background: #fdfdfd;
  }
  .loading-text {
    text-align: center;
    padding: 50px;
    font-family: 'Courier New', Courier, monospace;
    color: #666;
  }
---

## 游戏入口

直接在下方开始你的挑战。题目每 4 小时全服同步刷新一次。

<div class="l-page game-container">
  <iframe 
    src="https://redactle-chs.streamlit.app/?embed=true" 
    frameborder='0' 
    scrolling='yes' 
    height="800px" 
    width="100%"
    style="border: none;"
  >
    <p>您的浏览器不支持 iframe，请<a href="https://redactle-chs.streamlit.app/">点击此处</a>直接访问。</p>
  </iframe>
</div>

---

## 技术架构

本项目不仅仅是一个游戏，它是一个**无服务器自治系统**的实验。

### 系统流程

利用 Mermaid 渲染的系统拓扑图：

```mermaid
graph LR
    A[GitHub Actions] -- 定时触发 --> B[Streamlit Cloud]
    B -- 请求 --> C[NVIDIA NIM API]
    C -- 生成百科词条 --> B
    B -- 实时渲染 --> D[用户浏览器]
    D -- 交互反馈 --> B