(window.webpackJsonp=window.webpackJsonp||[]).push([[3],{RXBc:function(e,a,t){"use strict";t.r(a),t.d(a,"query",(function(){return w}));t("KKXr");var n=t("q1tI"),r=t.n(n),l=t("7vrA"),i=t("3Z9Z"),s=t("JI6e"),c=t("wx14"),o=t("zLVn"),u=t("TSYQ"),d=t.n(u),m=t("vUet"),f=r.a.forwardRef((function(e,a){var t,n=e.as,l=void 0===n?"div":n,i=e.className,s=e.fluid,u=e.bsPrefix,f=Object(o.a)(e,["as","className","fluid","bsPrefix"]),p=((t={})[u=Object(m.a)(u,"jumbotron")]=!0,t[u+"-fluid"]=s,t);return r.a.createElement(l,Object(c.a)({ref:a},f,{className:d()(i,p)}))}));f.defaultProps={fluid:!1},f.displayName="Jumbotron";var p=f,b=(t("a1Th"),t("Btvt"),t("I5cv"),t("f3/d"),t("dRSK"),t("h+2l")),h=t("Wbzz"),v=r.a.forwardRef((function(e,a){var t=e.bsPrefix,n=e.className,l=e.fluid,i=e.rounded,s=e.roundedCircle,u=e.thumbnail,f=Object(o.a)(e,["bsPrefix","className","fluid","rounded","roundedCircle","thumbnail"]);t=Object(m.a)(t,"img");var p=d()(l&&t+"-fluid",i&&"rounded",s&&"rounded-circle",u&&t+"-thumbnail");return r.a.createElement("img",Object(c.a)({ref:a},f,{className:d()(n,p)}))}));v.displayName="Image",v.defaultProps={fluid:!1,rounded:!1,roundedCircle:!1,thumbnail:!1};var g=v;var y=function(e){var a,t;t=e,(a=l).prototype=Object.create(t.prototype),a.prototype.constructor=a,a.__proto__=t;var n;n=l;function l(a){var t;return(t=e.call(this,a)||this).render_data=function(e){var a=e.allFile.edges.find((function(e){return e.node.name===t.props.image}));return console.log(e),console.log(a),r.a.createElement(i.a,null,r.a.createElement(s.a,{sm:8},r.a.createElement(g,{src:a.node.publicURL,fluid:!0})),r.a.createElement(s.a,{sm:4},r.a.createElement("h3",null,t.props.title),r.a.createElement("div",{dangerouslySetInnerHTML:{__html:t.props.content}})))},t}return l.prototype.render=function(){var e=this;return r.a.createElement(h.StaticQuery,{query:"1842141974",render:function(a){return e.render_data(a)},data:b})},l}(n.Component),E=t("Bl7J"),_=t("vrFN"),w=(a.default=function(e){var a=e.data;return r.a.createElement(E.a,{pageInfo:{pageName:"index"}},r.a.createElement(_.a,{title:"Home",keywords:["gatsby","react","bootstrap"]}),r.a.createElement(l.a,{className:"text-center"},r.a.createElement(i.a,null,r.a.createElement(s.a,null,r.a.createElement("p",null,"This page tries to visualize the COVID-19 data provided by the Johns Hopkins University."),r.a.createElement("p",null,"While many pages visualize the current data on different levels, I have not yet seen any page that tries to focus on visualizing the timeline on a per-country level. This page shows the results of my visualizations."),r.a.createElement(p,null,r.a.createElement("strong",null,"Disclaimer"),": This page only is meant to display the data gathered by the Johns Hopkins University. I hereby disclaim any and all representations and warranties with respect to the Website, including accuracy, fitness for use, and merchantability. Reliance on the Website for medical guidance or use of the Website in commerce is strictly prohibited."))),a.allMarkdownRemark.edges.map((function(e,a){var t=e.node,n=t.fileAbsolutePath.split("/"),l=n[n.length-1];return console.log(l.split(".")[0]),r.a.createElement(y,{key:"POST_"+a,image:l.split(".")[0],title:t.frontmatter.title,content:t.html})}))))},"3095619974")},"h+2l":function(e){e.exports=JSON.parse('{"data":{"allFile":{"edges":[{"node":{"publicURL":"/COVID-19/static/aebf9615051df38451c6bb3d4320fd8a/rates_small.png","name":"rates_small"}},{"node":{"publicURL":"/COVID-19/static/81715feb319fe27591ecac6ef8f6561a/rates.png","name":"rates"}},{"node":{"publicURL":"/COVID-19/static/f7c3d3ca7a29b6c3353736b3eff548ea/basic_numbers_small.png","name":"basic_numbers_small"}},{"node":{"publicURL":"/COVID-19/static/538badd9adf39eb88c4097f7fe7cfa44/basic_numbers.png","name":"basic_numbers"}}]}}}')}}]);
//# sourceMappingURL=component---src-pages-index-js-3831b69cc444adf91d8e.js.map