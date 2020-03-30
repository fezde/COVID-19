(window.webpackJsonp=window.webpackJsonp||[]).push([[3],{RXBc:function(e,a,t){"use strict";t.r(a),t.d(a,"query",(function(){return O}));t("hEkN"),t("KKXr");var n=t("q1tI"),r=t.n(n),l=t("7vrA"),s=t("3Z9Z"),i=t("JI6e"),o=t("wx14"),c=t("zLVn"),d=t("TSYQ"),m=t.n(d),u=t("vUet"),f=r.a.forwardRef((function(e,a){var t,n=e.as,l=void 0===n?"div":n,s=e.className,i=e.fluid,d=e.bsPrefix,f=Object(c.a)(e,["as","className","fluid","bsPrefix"]),p=((t={})[d=Object(u.a)(d,"jumbotron")]=!0,t[d+"-fluid"]=i,t);return r.a.createElement(l,Object(o.a)({ref:a},f,{className:m()(s,p)}))}));f.defaultProps={fluid:!1},f.displayName="Jumbotron";var p=f,b=(t("a1Th"),t("Btvt"),t("I5cv"),t("f3/d"),t("dRSK"),t("h+2l")),h=t("Wbzz"),g=r.a.forwardRef((function(e,a){var t=e.bsPrefix,n=e.className,l=e.fluid,s=e.rounded,i=e.roundedCircle,d=e.thumbnail,f=Object(c.a)(e,["bsPrefix","className","fluid","rounded","roundedCircle","thumbnail"]);t=Object(u.a)(t,"img");var p=m()(l&&t+"-fluid",s&&"rounded",i&&"rounded-circle",d&&t+"-thumbnail");return r.a.createElement("img",Object(o.a)({ref:a},f,{className:m()(n,p)}))}));g.displayName="Image",g.defaultProps={fluid:!1,rounded:!1,roundedCircle:!1,thumbnail:!1};var v=g;var y=function(e){var a,t;t=e,(a=l).prototype=Object.create(t.prototype),a.prototype.constructor=a,a.__proto__=t;var n;n=l;function l(a){var t;return(t=e.call(this,a)||this).render_data=function(e){var a=e.allFile.edges.find((function(e){return e.node.name===t.props.image+"_small"})),n=e.allFile.edges.find((function(e){return e.node.name===t.props.image}));console.log(e),console.log(n);var l=r.a.createElement(i.a,{sm:12,lg:8},r.a.createElement("a",{name:t.props.anchor,style:{fontSize:"0.8em"},onClick:function(e){t.setState({showOverlay:!t.state.showOverlay})},href:"#"},r.a.createElement(v,{src:a.node.publicURL,fluid:!0}),r.a.createElement("br",null),"(Click to enlarge)")),o="order-sm-last";"left"===t.props.align&&(o="order-sm-last order-lg-first");var c=r.a.createElement(i.a,{sm:12,lg:4,className:o},r.a.createElement("h3",{className:"d-none d-lg-block"},t.props.title,"- ",t.props.align),r.a.createElement("div",{style:{textAlign:"left"},dangerouslySetInnerHTML:{__html:t.props.content}}));return r.a.createElement(r.a.Fragment,null,r.a.createElement(s.a,{id:t.props.anchor,className:"shadow-sm"},r.a.createElement("div",{style:{background:"#000000af",position:"fixed",width:"100vw",height:"100vh",top:0,left:0,zIndex:1e3,display:t.state.showOverlay?"block":"none"},onClick:function(e){t.setState({showOverlay:!t.state.showOverlay})}},r.a.createElement(v,{src:n.node.publicURL,fluid:!0,style:{maxWidth:"90vw",position:"absolute",left:"50vw",top:"50vh",transform:"translate(-50%, -50%)"}})),r.a.createElement(i.a,{sm:12,className:"d-block d-lg-none"},r.a.createElement("h3",null,t.props.title)),l,c),r.a.createElement(s.a,null,r.a.createElement(i.a,{style:{minHeight:"40px"}}," ")))},t.state={showOverlay:!1},t}return l.prototype.render=function(){var e=this;return r.a.createElement(r.a.Fragment,null,r.a.createElement(h.StaticQuery,{query:"1842141974",render:function(a){return e.render_data(a)},data:b}))},l}(n.Component),E=t("Bl7J"),w=t("vrFN"),O=(a.default=function(e){var a=e.data,t=0;return r.a.createElement(E.a,{pageInfo:{pageName:"index"}},r.a.createElement(w.a,{title:"Home",keywords:["gatsby","react","bootstrap"]}),r.a.createElement(l.a,{className:"text-center"},r.a.createElement(s.a,null,r.a.createElement(i.a,null,r.a.createElement("p",null,"This page aims to visualize the COVID-19 pandemy using data provided by the Johns Hopkins University."),r.a.createElement("p",null,"While many pages visualize the current data on different levels, I have not yet seen any page that tries to focus on visualizing the timeline on a per-country level. This page shows the results of my visualizations."),r.a.createElement(p,null,r.a.createElement("strong",null,"Disclaimer"),": This page only is meant to display the data gathered by the Johns Hopkins University. I hereby disclaim any and all representations and warranties with respect to the Website, including accuracy, fitness for use, and merchantability. Reliance on the Website for medical guidance or use of the Website in commerce is strictly prohibited."))),a.allMarkdownRemark.edges.map((function(e,a){var n=e.node,l=n.fileAbsolutePath.split("/"),s=l[l.length-1];return console.log(s.split(".")[0]),r.a.createElement(y,{key:"POST_"+a,image:s.split(".")[0],title:n.frontmatter.title,anchor:n.frontmatter.anchor,content:n.html,align:++t%2==0?"left":"right"})}))))},"3950266204")},"h+2l":function(e){e.exports=JSON.parse('{"data":{"allFile":{"edges":[{"node":{"publicURL":"/COVID-19/static/82c5e4250569c0674692b9dce3548f15/offsets_small.png","name":"offsets_small"}},{"node":{"publicURL":"/COVID-19/static/7964d54f6b2a75d33d6376b7fef446f0/offsets.png","name":"offsets"}},{"node":{"publicURL":"/COVID-19/static/d9488c3ebcc379a0d807a12e1e7567c7/basic_numbers_small.png","name":"basic_numbers_small"}},{"node":{"publicURL":"/COVID-19/static/689ecfca3fad27b4502dccdb2563914b/basic_numbers.png","name":"basic_numbers"}},{"node":{"publicURL":"/COVID-19/static/57bbea99db0b488aa582aba9a2ec3f11/rates_small.png","name":"rates_small"}},{"node":{"publicURL":"/COVID-19/static/c69bf7ef0bd6773c91bba92c371fc670/rates.png","name":"rates"}}]}}}')},hEkN:function(e,a,t){"use strict";t("OGtf")("anchor",(function(e){return function(a){return e(this,"a","name",a)}}))}}]);
//# sourceMappingURL=component---src-pages-index-js-995d42390cc5fca227c2.js.map