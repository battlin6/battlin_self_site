define("discourse/plugins/discourse-ai/discourse/routes/admin-plugins-show-discourse-ai-llms-new",["exports","discourse/routes/discourse"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=s.default.extend({async model(){return this.store.createRecord("ai-llm")},setupController(e,s){this._super(e,s),e.set("allLlms",this.modelFor("adminPlugins.show.discourse-ai-llms"))}})})),define("discourse/plugins/discourse-ai/discourse/routes/admin-plugins-show-discourse-ai-llms-show",["exports","discourse/routes/discourse"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=s.default.extend({async model(e){const s=this.modelFor("adminPlugins.show.discourse-ai-llms"),o=parseInt(e.id,10)
return s.findBy("id",o)},setupController(e,s){this._super(e,s),e.set("allLlms",this.modelFor("adminPlugins.show.discourse-ai-llms"))}})})),define("discourse/plugins/discourse-ai/discourse/routes/admin-plugins-show-discourse-ai-llms",["exports","discourse/routes/discourse"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
class o extends s.default{model(){return this.store.findAll("ai-llm")}}e.default=o})),define("discourse/plugins/discourse-ai/discourse/routes/admin-plugins-show-discourse-ai-personas-new",["exports","discourse/lib/constants","discourse/routes/discourse"],(function(e,s,o){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=o.default.extend({async model(){const e=this.store.createRecord("ai-persona")
return e.set("allowed_group_ids",[s.AUTO_GROUPS.trust_level_0.id]),e.set("rag_uploads",[]),e.set("rag_chunk_tokens",374),e.set("rag_chunk_overlap_tokens",10),e.set("rag_conversation_chunks",10),e},setupController(e,s){this._super(e,s),e.set("allPersonas",this.modelFor("adminPlugins.show.discourse-ai-personas"))}})})),define("discourse/plugins/discourse-ai/discourse/routes/admin-plugins-show-discourse-ai-personas-show",["exports","discourse/routes/discourse"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=s.default.extend({async model(e){const s=this.modelFor("adminPlugins.show.discourse-ai-personas"),o=parseInt(e.id,10)
return s.findBy("id",o)},setupController(e,s){this._super(e,s),e.set("allPersonas",this.modelFor("adminPlugins.show.discourse-ai-personas"))}})})),define("discourse/plugins/discourse-ai/discourse/routes/admin-plugins-show-discourse-ai-personas",["exports","discourse/routes/discourse"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
class o extends s.default{model(){return this.store.findAll("ai-persona")}}e.default=o})),define("discourse/plugins/discourse-ai/discourse/routes/admin-plugins-show-discourse-ai-tools-new",["exports","discourse/routes/discourse"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
class o extends s.default{async model(){return this.store.createRecord("ai-tool")}setupController(e){super.setupController(...arguments)
const s=this.modelFor("adminPlugins.show.discourse-ai-tools")
e.set("allTools",s),e.set("presets",s.resultSetMeta.presets)}}e.default=o})),define("discourse/plugins/discourse-ai/discourse/routes/admin-plugins-show-discourse-ai-tools-show",["exports","discourse/routes/discourse"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
class o extends s.default{async model(e){const s=this.modelFor("adminPlugins.show.discourse-ai-tools"),o=parseInt(e.id,10)
return s.find((e=>e.id===o))}setupController(e){super.setupController(...arguments)
const s=this.modelFor("adminPlugins.show.discourse-ai-tools")
e.set("allTools",s),e.set("presets",s.resultSetMeta.presets)}}e.default=o})),define("discourse/plugins/discourse-ai/discourse/routes/admin-plugins-show-discourse-ai-tools",["exports","@ember/service","discourse/routes/discourse"],(function(e,s,o){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
class i extends o.default{static#e=(()=>dt7948.g(this.prototype,"store",[s.service]))()
#s=(()=>{dt7948.i(this,"store")})()
model(){return this.store.findAll("ai-tool")}}e.default=i})),define("discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-llms/index",["exports","@ember/template-factory"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=(0,s.createTemplateFactory)({id:"/hpMWqzQ",block:'[[[8,[39,0],null,[["@llms"],[[30,0,["model"]]]],null]],[],false,["ai-llms-list-editor"]]',moduleName:"discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-llms/index.hbs",isStrictMode:!1})})),define("discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-llms/new",["exports","@ember/template-factory"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=(0,s.createTemplateFactory)({id:"LNPU2H/h",block:'[[[8,[39,0],null,[["@llms","@currentLlm"],[[30,0,["allLlms"]],[30,0,["model"]]]],null]],[],false,["ai-llms-list-editor"]]',moduleName:"discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-llms/new.hbs",isStrictMode:!1})})),define("discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-llms/show",["exports","@ember/template-factory"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=(0,s.createTemplateFactory)({id:"tdQ3gCh/",block:'[[[8,[39,0],null,[["@llms","@currentLlm"],[[30,0,["allLlms"]],[30,0,["model"]]]],null]],[],false,["ai-llms-list-editor"]]',moduleName:"discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-llms/show.hbs",isStrictMode:!1})})),define("discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-personas/index",["exports","@ember/template-factory"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=(0,s.createTemplateFactory)({id:"S3ls7MhI",block:'[[[8,[39,0],null,[["@personas"],[[30,0,["model"]]]],null]],[],false,["ai-persona-list-editor"]]',moduleName:"discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-personas/index.hbs",isStrictMode:!1})})),define("discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-personas/new",["exports","@ember/template-factory"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=(0,s.createTemplateFactory)({id:"uPcey72d",block:'[[[8,[39,0],null,[["@personas","@currentPersona"],[[30,0,["allPersonas"]],[30,0,["model"]]]],null]],[],false,["ai-persona-list-editor"]]',moduleName:"discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-personas/new.hbs",isStrictMode:!1})})),define("discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-personas/show",["exports","@ember/template-factory"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=(0,s.createTemplateFactory)({id:"vhi53gxi",block:'[[[8,[39,0],null,[["@personas","@currentPersona"],[[30,0,["allPersonas"]],[30,0,["model"]]]],null]],[],false,["ai-persona-list-editor"]]',moduleName:"discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-personas/show.hbs",isStrictMode:!1})})),define("discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-tools/index",["exports","@ember/template-factory"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=(0,s.createTemplateFactory)({id:"jeGs6+Fr",block:'[[[8,[39,0],null,[["@tools"],[[30,0,["model"]]]],null]],[],false,["ai-tool-list-editor"]]',moduleName:"discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-tools/index.hbs",isStrictMode:!1})})),define("discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-tools/new",["exports","@ember/template-factory"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=(0,s.createTemplateFactory)({id:"XEXgGI/R",block:'[[[8,[39,0],null,[["@tools","@model","@presets"],[[30,0,["allTools"]],[30,0,["model"]],[30,0,["presets"]]]],null]],[],false,["ai-tool-editor"]]',moduleName:"discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-tools/new.hbs",isStrictMode:!1})})),define("discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-tools/show",["exports","@ember/template-factory"],(function(e,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=(0,s.createTemplateFactory)({id:"oCPGCpJ0",block:'[[[8,[39,0],null,[["@tools","@model","@presets"],[[30,0,["allTools"]],[30,0,["model"]],[30,0,["presets"]]]],null]],[],false,["ai-tool-editor"]]',moduleName:"discourse/plugins/discourse-ai/discourse/templates/admin-plugins/show/discourse-ai-tools/show.hbs",isStrictMode:!1})}))

//# sourceMappingURL=discourse-ai_admin-7c910a2f5a39c553dc9d1ccada31c5bbe3bc49625c53d41a64675905a5ef98cd.map
//!

;
