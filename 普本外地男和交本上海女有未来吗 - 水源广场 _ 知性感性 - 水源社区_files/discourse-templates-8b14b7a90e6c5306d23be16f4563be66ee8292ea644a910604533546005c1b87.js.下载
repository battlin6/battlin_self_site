define("discourse/plugins/discourse-templates/discourse/components/d-templates/filterable-list",["exports","@ember/component","@glimmer/component","@glimmer/tracking","@ember/object","@ember/runloop","@ember/service","discourse/lib/ajax","discourse/lib/ajax-error","discourse-common/utils/decorators","select-kit/components/tag-drop","@ember/template-factory"],(function(e,t,s,o,i,a,l,r,n,c,d,p){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
const u=(0,p.createTemplateFactory)({id:"MxdRx2Ru",block:'[[[11,0],[24,0,"templates-filterable-list"],[4,[38,0],[[30,0,["load"]]],null],[12],[1,"\\n\\n  "],[8,[39,1],null,[["@condition"],[[30,0,["loading"]]]],[["default"],[[[[1,"\\n    "],[10,0],[14,0,"templates-filter-bar"],[12],[1,"\\n"],[41,[30,0,["siteSettings","tagging_enabled"]],[[[1,"        "],[8,[39,3],null,[["@availableTags","@tagId","@onChangeSelectedTag"],[[30,0,["availableTags"]],[30,0,["selectedTag"]],[30,0,["changeSelectedTag"]]]],null],[1,"\\n"]],[]],null],[1,"      "],[8,[39,4],[[24,0,"templates-filter"],[16,"placeholder",[28,[37,5],["templates.filter_hint"],null]]],[["@value"],[[30,0,["listFilter"]]]],null],[1,"\\n    "],[13],[1,"\\n    "],[10,0],[14,0,"templates-list"],[12],[1,"\\n"],[42,[28,[37,7],[[28,[37,7],[[30,0,["filteredReplies"]]],null]],null],null,[[[1,"        "],[8,[39,8],null,[["@template","@model","@onInsertTemplate"],[[30,1],[30,2],[30,0,["insertTemplate"]]]],null],[1,"\\n"]],[1]],null],[1,"    "],[13],[1,"\\n  "]],[]]]]],[1,"\\n"],[13]],["r","@model"],false,["did-insert","conditional-loading-spinner","if","d-templates/tag-drop","text-field","i18n","each","-track-array","d-templates/item"]]',moduleName:"discourse/plugins/discourse-templates/discourse/components/d-templates/filterable-list.hbs",isStrictMode:!1})
class m extends s.default{static#e=(()=>dt7948.g(this.prototype,"siteSettings",[l.inject]))()
#t=(()=>{dt7948.i(this,"siteSettings")})()
static#s=(()=>dt7948.g(this.prototype,"loading",[o.tracked],(function(){return!0})))()
#o=(()=>{dt7948.i(this,"loading")})()
static#i=(()=>dt7948.g(this.prototype,"listFilter",[o.tracked],(function(){return""})))()
#a=(()=>{dt7948.i(this,"listFilter")})()
static#l=(()=>dt7948.g(this.prototype,"replies",[o.tracked],(function(){return[]})))()
#r=(()=>{dt7948.i(this,"replies")})()
static#n=(()=>dt7948.g(this.prototype,"selectedTag",[o.tracked],(function(){return d.ALL_TAGS_ID})))()
#c=(()=>{dt7948.i(this,"selectedTag")})()
static#d=(()=>dt7948.g(this.prototype,"availableTags",[o.tracked],(function(){return[]})))()
#p=(()=>{dt7948.i(this,"availableTags")})()
get filteredReplies(){const e=this.listFilter.toLowerCase()
return this.replies.map((t=>(t.score=0,t.title.toLowerCase().includes(e)?t.score+=2:t.content.toLowerCase().includes(e)&&(t.score+=1),t))).filter((e=>0!==e.score)).filter((e=>this.selectedTag===d.ALL_TAGS_ID||(this.selectedTag===d.NO_TAG_ID&&0===e.tags.length||e.tags.includes(this.selectedTag)))).sort(((e,t)=>e.score!==t.score?e.score>t.score?-1:1:e.title!==t.title?e.title<t.title?-1:1:0))}static#u=(()=>dt7948.n(this.prototype,"filteredReplies",[(0,i.computed)("replies","selectedTag","listFilter")]))()
async load(){try{this.loading=!0
const e=await(0,r.ajax)("/discourse_templates")
this.replies=e.templates,this.siteSettings.tagging_enabled&&(this.availableTags=Object.values(this.replies.reduce(((e,t)=>(t.tags.forEach((t=>{e[t]?e[t].count+=1:e[t]={id:t,name:t,count:1}})),e)),{})))}catch(e){this.loading=!1,(0,n.popupAjaxError)(e)}finally{this.loading=!1,(0,a.schedule)("afterRender",(()=>document.querySelector(".templates-filter")?.focus()))}}static#m=(()=>dt7948.n(this.prototype,"load",[c.bind]))()
changeSelectedTag(e){this.selectedTag=e}static#h=(()=>dt7948.n(this.prototype,"changeSelectedTag",[i.action]))()
insertTemplate(e){this.args.onBeforeInsertTemplate?.(),this.args.onInsertTemplate?.(e),this.args.onAfterInsertTemplate?.()}static#f=(()=>dt7948.n(this.prototype,"insertTemplate",[i.action]))()}e.default=m,(0,t.setComponentTemplate)(u,m)})),define("discourse/plugins/discourse-templates/discourse/components/d-templates/item-content",["exports","@ember/component","@ember/component/template-only","@ember/template-factory"],(function(e,t,s,o){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
const i=(0,o.createTemplateFactory)({id:"r2J+FHK0",block:'[[[10,0],[14,0,"templates-content"],[12],[1,"\\n  "],[8,[39,0],[[24,0,"template-item-source-link"]],[["@route","@models"],["topic",[28,[37,1],[[30,1,["slug"]],[30,1,["id"]]],null]]],[["default"],[[[[1,"\\n    "],[1,[28,[35,2],["crosshairs"],null]],[1,"\\n    "],[1,[28,[35,3],["templates.source"],null]],[1,"\\n  "]],[]]]]],[1,"\\n  "],[8,[39,4],null,[["@rawText"],[[30,1,["content"]]]],null],[1,"\\n"],[13]],["@template"],false,["link-to","array","d-icon","i18n","cook-text"]]',moduleName:"discourse/plugins/discourse-templates/discourse/components/d-templates/item-content.hbs",isStrictMode:!1})
e.default=(0,t.setComponentTemplate)(i,(0,s.default)())})),define("discourse/plugins/discourse-templates/discourse/components/d-templates/item",["exports","@ember/component","@glimmer/component","@ember/object","discourse/lib/ajax","discourse/lib/ajax-error","@ember/template-factory"],(function(e,t,s,o,i,a,l){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
const r=(0,l.createTemplateFactory)({id:"6/xlvlVX",block:'[[[10,"details"],[14,0,"template-item"],[15,1,[29,["template-item-",[30,1,["id"]]]]],[12],[1,"\\n  "],[10,"summary"],[14,0,"template-item-title"],[12],[1,"\\n    "],[10,0],[14,0,"template-item-title-text"],[12],[1,[30,1,["title"]]],[13],[1,"\\n\\n    "],[10,0],[14,0,"actions"],[12],[1,"\\n      "],[8,[39,0],[[24,0,"templates-apply"]],[["@action","@icon"],[[28,[37,1],[[30,0],"apply"],null],"far-clipboard"]],null],[1,"\\n    "],[13],[1,"\\n  "],[13],[1,"\\n\\n  "],[8,[39,2],null,[["@template"],[[30,1]]],null],[1,"\\n"],[13]],["@template"],false,["d-button","action","d-templates/item-content"]]',moduleName:"discourse/plugins/discourse-templates/discourse/components/d-templates/item.hbs",isStrictMode:!1})
class n extends s.default{apply(){this.args.onInsertTemplate?.(this.args.template),(0,i.ajax)(`/discourse_templates/${this.args.template.id}/use`,{type:"POST"}).catch(a.popupAjaxError)}static#e=(()=>dt7948.n(this.prototype,"apply",[o.action]))()}e.default=n,(0,t.setComponentTemplate)(r,n)})),define("discourse/plugins/discourse-templates/discourse/components/d-templates/modal/form",["exports","@ember/component","@glimmer/component","@ember/service","@ember/template-factory"],(function(e,t,s,o,i){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
const a=(0,i.createTemplateFactory)({id:"StqqkQ0S",block:'[[[8,[39,0],[[24,0,"d-templates d-templates-modal"]],[["@closeModal","@title"],[[30,1],[28,[37,1],["templates.insert_template"],null]]],[["body"],[[[[1,"\\n    "],[8,[39,2],null,[["@textarea","@onInsertTemplate","@onAfterInsertTemplate"],[[30,2,["textarea"]],[30,2,["onInsertTemplate"]],[30,1]]],null],[1,"\\n  "]],[]]]]]],["@closeModal","@model"],false,["d-modal","i18n","d-templates/filterable-list"]]',moduleName:"discourse/plugins/discourse-templates/discourse/components/d-templates/modal/form.hbs",isStrictMode:!1})
class l extends s.default{static#e=(()=>dt7948.g(this.prototype,"appEvents",[o.service]))()
#g=(()=>{dt7948.i(this,"appEvents")})()
constructor(){super(...arguments),this.args.closeModal&&this.appEvents.on("page:changed",this,this.args.closeModal)}willDestroy(){super.willDestroy(...arguments),this.args.closeModal&&this.appEvents.off("page:changed",this,this.args.closeModal)}}e.default=l,(0,t.setComponentTemplate)(a,l)})),define("discourse/plugins/discourse-templates/discourse/components/d-templates/tag-drop",["exports","@ember/object","select-kit/components/tag-drop"],(function(e,t,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
class o extends s.default{get topTags(){return(this.availableTags||[]).sort(((e,t)=>e.count!==t.count?t.count-e.count:e.name!==t.name?e.name<t.name?-1:1:0))}static#e=(()=>dt7948.n(this.prototype,"topTags",[(0,t.computed)("availableTags.[]")]))()
search(e){return(this.content||[]).map((e=>e.id&&e.name?e:this.defaultItem(e,e))).filter((t=>{if(null==e)return!0
const s=e.toLowerCase()
return t.id.toLowerCase().includes(s)||t.name.toLowerCase().includes(s)}))}onChange(e,t){this.onChangeSelectedTag?.(e,t)}static#s=(()=>dt7948.n(this.prototype,"onChange",[t.action]))()}e.default=o})),define("discourse/plugins/discourse-templates/discourse/connectors/below-footer/d-templates-modal-container",["exports","@glimmer/component","@ember/service","discourse/plugins/discourse-templates/discourse/components/d-templates/modal/form","@ember/component","@ember/template-factory"],(function(e,t,s,o,i,a){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
class l extends t.default{static#e=(()=>dt7948.g(this.prototype,"dTemplatesModal",[s.inject]))()
#_=(()=>{dt7948.i(this,"dTemplatesModal")})()
static#s=(()=>(0,i.setComponentTemplate)((0,a.createTemplateFactory)({id:"9ouJ2oOR",block:'[[[1,"\\n"],[41,[30,0,["dTemplatesModal","model"]],[[[1,"      "],[10,0],[14,0,"modal-container d-templates-modal-container"],[12],[1,"\\n        "],[8,[32,0],null,[["@closeModal","@model"],[[30,0,["dTemplatesModal","hide"]],[30,0,["dTemplatesModal","model"]]]],null],[1,"\\n      "],[13],[1,"\\n"]],[]],null],[1,"  "]],[],false,["if"]]',moduleName:"/var/www/discourse/app/assets/javascripts/discourse/discourse/plugins/discourse-templates/discourse/connectors/below-footer/d-templates-modal-container.js",scope:()=>[o.default],isStrictMode:!0}),this))()}e.default=l})),define("discourse/plugins/discourse-templates/discourse/connectors/editor-preview/d-templates",["exports","@ember/object","discourse-common/lib/get-owner"],(function(e,t,s){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
const o="#reply-control .d-editor-preview-wrapper > .d-editor-preview"
e.default=dt7948.p({setupComponent(e,t){t.setProperties({templatesVisible:!1,model:(0,s.getOwnerWithFallback)(this).lookup("controller:composer").model}),this.appEvents.on("discourse-templates:show",this,"show"),this.appEvents.on("discourse-templates:hide",this,"hide")},teardownComponent(){this.appEvents.off("discourse-templates:show",this,"show"),this.appEvents.off("discourse-templates:hide",this,"hide")},shouldRender:(e,t)=>!t.site.mobileView,show(e){let{onInsertTemplate:t}=e
const s=document.querySelector(o)
s&&(s.style.display="none"),this.set("onInsertTemplate",t),this.set("templatesVisible",!0)},hide(){const e=document.querySelector(o)
e&&(e.style.display=""),this.set("templatesVisible",!1)}},[["method","show",[t.action]],["method","hide",[t.action]]])})),define("discourse/plugins/discourse-templates/discourse/connectors/topic-above-posts/discourse-templates-button",["exports","@glimmer/component","@glimmer/tracking","@ember/object","@ember/service","discourse/lib/ajax","discourse-common/lib/debounce"],(function(e,t,s,o,i,a,l){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
class r extends t.default{static shouldRender(e,t){return e.model.is_template&&t.currentUser?.can_create_topic}static#e=(()=>dt7948.g(this.prototype,"composer",[i.inject]))()
#b=(()=>{dt7948.i(this,"composer")})()
static#s=(()=>dt7948.g(this.prototype,"copyConfirm",[s.tracked],(function(){return!1})))()
#y=(()=>{dt7948.i(this,"copyConfirm")})()
async fetchRaw(){const e=this.args.outletArgs.model
return await(0,a.ajax)(`/raw/${e.id}/1`,{dataType:"text"})}async createNewTopic(){const e=await this.fetchRaw()
this.composer.openNewTopic({body:e})}static#i=(()=>dt7948.n(this.prototype,"createNewTopic",[o.action]))()
async copy(){const e=await this.fetchRaw()
navigator.clipboard.writeText(e),this.copyConfirm=!0,(0,l.default)(this.resetCopyButton,2e3)}static#l=(()=>dt7948.n(this.prototype,"copy",[o.action]))()
resetCopyButton(){this.copyConfirm=!1}static#n=(()=>dt7948.n(this.prototype,"resetCopyButton",[o.action]))()}e.default=r})),define("discourse/plugins/discourse-templates/discourse/initializers/d-templates",["exports","discourse/lib/keyboard-shortcuts","discourse/lib/plugin-api","discourse-common/lib/get-owner","discourse/plugins/discourse-templates/lib/variables-chat-channel","discourse/plugins/discourse-templates/lib/variables-chat-thread"],(function(e,t,s,o,i,a){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default={name:"discourse-templates-add-ui-builder",initialize(e){const r=e.lookup("service:site-settings"),n=e.lookup("service:current-user")
r.discourse_templates_enabled&&n?.can_use_templates&&(0,s.withPluginApi)("1.13.0",(s=>{(function(e){const t=e.container.lookup("service:d-templates")
e.addComposerToolbarPopupMenuOption({icon:"far-clipboard",label:"templates.insert_template",action:()=>{t.showComposerUI()}})})(s),function(e,s){e.addKeyboardShortcut(`${t.PLATFORM_KEY_MODIFIER}+shift+i`,(e=>{e.preventDefault()
const t=s.lookup("service:d-templates")
if(t.isComposerFocused)t.showComposerUI()
else{for(const e of l)if(t.isTextAreaFocused&&e?.isFocused?.(document.activeElement))return void t.showTextAreaUI(e?.variables)
t.isTextAreaFocused&&t.showTextAreaUI()}}),{global:!0,help:{category:"templates",name:"templates.insert_template",definition:{keys1:[t.PLATFORM_KEY_MODIFIER,"shift","I"],keysDelimiter:"plus"}}})}(s,e),function(e,t){if(!t.lookup("service:chat")?.userCanChat)return
const s=function(){const e=(0,o.getOwnerWithFallback)(this).lookup("service:chat"),t=e?.activeChannel,s=t?.draft,a=(0,o.getOwnerWithFallback)(this).lookup("service:router")
return(0,i.default)(t,s,a)},r=function(){const e=(0,o.getOwnerWithFallback)(this).lookup("service:chat"),t=e?.activeChannel?.activeThread,s=t?.draft,i=(0,o.getOwnerWithFallback)(this).lookup("service:router")
return(0,a.default)(t,s,i)}
e.registerChatComposerButton({id:"d-templates-chat-insert-template-btn",icon:"far-clipboard",label:"templates.insert_template",position:"dropdown",action:function(){let e
switch(this.context){case"channel":e=s.bind(this)
break
case"thread":e=r.bind(this)
break
default:e=null}const t=this.composer?.textarea?.textarea;(0,o.getOwnerWithFallback)(this).lookup("service:d-templates").showTextAreaUI(e,t)},displayed(){return this.composer?.textarea&&("channel"===this.context||"thread"===this.context)}}),l.push({isFocused:e=>"channel-composer"===e?.id,variables:s},{isFocused:e=>"thread-composer"===e?.id,variables:r})}(s,e)}))}}
const l=[]})),define("discourse/plugins/discourse-templates/discourse/services/d-templates-modal",["exports","@glimmer/tracking","@ember/object","@ember/service"],(function(e,t,s,o){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
class i extends o.default{static#e=(()=>dt7948.g(this.prototype,"model",[t.tracked],(function(){return null})))()
#v=(()=>{dt7948.i(this,"model")})()
show(e){this.model=e}static#s=(()=>dt7948.n(this.prototype,"show",[s.action]))()
hide(){this.model?.textarea?.focus(),this.model=null}static#i=(()=>dt7948.n(this.prototype,"hide",[s.action]))()}e.default=i})),define("discourse/plugins/discourse-templates/discourse/services/d-templates",["exports","@ember/application","@ember/service","discourse/plugins/discourse-templates/lib/replace-variables","discourse/plugins/discourse-templates/lib/textarea-manipulator","discourse/plugins/discourse-templates/lib/variables-composer"],(function(e,t,s,o,i,a){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
class l extends s.default{static#e=(()=>dt7948.g(this.prototype,"appEvents",[s.inject]))()
#g=(()=>{dt7948.i(this,"appEvents")})()
static#s=(()=>dt7948.g(this.prototype,"modal",[s.inject]))()
#T=(()=>{dt7948.i(this,"modal")})()
static#i=(()=>dt7948.g(this.prototype,"site",[s.inject]))()
#x=(()=>{dt7948.i(this,"site")})()
static#l=(()=>dt7948.g(this.prototype,"currentUser",[s.inject]))()
#w=(()=>{dt7948.i(this,"currentUser")})()
static#n=(()=>dt7948.g(this.prototype,"dTemplatesModal",[s.inject]))()
#_=(()=>{dt7948.i(this,"dTemplatesModal")})()
showComposerUI(){const e=this.#M.bind(this)
this.site.mobileView?this.#k(null,e):this.#j(e)}showTextAreaUI(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:null,t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:document.activeElement
if(!this.#E(t))return
const s=document.querySelector(".d-modal"),o=this.#C.bind(this),i=t=>e?.(t)
s?.contains(t)?s.classList.contains("d-templates")||this.#k(t,(e=>{const s=this.modal.activeModal?.opts?.model
o(t,e,i(s))})):this.#k(t,(e=>o(t,e,i())))}get isComposerFocused(){const e=document.activeElement,s=(0,t.getOwner)(this).lookup("controller:composer").model,o=document.querySelector(".d-editor")
return s&&o?.contains(e)}get isTextAreaFocused(){return this.#E(document.activeElement)}#E(e){return"TEXTAREA"===e?.nodeName}#I(e,t){this.appEvents.trigger("discourse-templates:hijack-modal",{textarea:e,onInsertTemplate:t})}#k(e,t){this.dTemplatesModal.show({textarea:e,onInsertTemplate:t})}#j(e){this.appEvents.trigger("composer-messages:close"),this.appEvents.trigger("composer:show-preview"),this.appEvents.trigger("discourse-templates:show",{onInsertTemplate:e})}#C(e,s,o){s=this.#O(s.title,s.content,o),new i.default((0,t.getOwner)(this),e).addBlock(s.content)}#M(e){const s=(0,t.getOwner)(this).lookup("controller:composer").model,o=(0,a.default)(s)
e=this.#O(e.title,e.content,o),s&&!s.title&&s.set("title",e.title),this.appEvents.trigger("composer:insert-block",e.content)}#O(e,t){let s=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{}
return(0,o.replaceVariables)(e,t,{...s,my_username:this.currentUser?.username,my_name:this.currentUser?.displayName})}}e.default=l})),define("discourse/plugins/discourse-templates/discourse/templates/connectors/editor-preview/d-templates",["exports","@ember/template-factory"],(function(e,t){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=(0,t.createTemplateFactory)({id:"IBGlp3aJ",block:'[[[41,[30,0,["templatesVisible"]],[[[1,"  "],[10,0],[14,0,"d-templates-container"],[12],[1,"\\n    "],[8,[39,1],[[24,0,"modal-close close btn-flat"]],[["@action","@icon"],[[28,[37,2],[[30,0],"hide"],null],"times"]],null],[1,"\\n    "],[8,[39,3],null,[["@onInsertTemplate","@onAfterInsertTemplate"],[[30,0,["onInsertTemplate"]],[28,[37,2],[[30,0],"hide"],null]]],null],[1,"\\n  "],[13],[1,"\\n"]],[]],null]],[],false,["if","d-button","action","d-templates/filterable-list"]]',moduleName:"discourse/plugins/discourse-templates/discourse/templates/connectors/editor-preview/d-templates.hbs",isStrictMode:!1})})),define("discourse/plugins/discourse-templates/discourse/templates/connectors/topic-above-posts/discourse-templates-button",["exports","@ember/template-factory"],(function(e,t){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
e.default=(0,t.createTemplateFactory)({id:"JxzWUf6/",block:'[[[10,0],[14,0,"template-topic-controls"],[12],[1,"\\n  "],[8,[39,0],[[16,0,[28,[37,1],["btn-default","template-copy",[52,[30,0,["copyConfirm"]],"ok"]],null]]],[["@icon","@action","@label"],[[52,[30,0,["copyConfirm"]],"check","copy"],[30,0,["copy"]],"templates.copy"]],null],[1,"\\n  "],[8,[39,0],[[24,0,"template-new-topic"]],[["@action","@label","@icon"],[[30,0,["createNewTopic"]],"templates.new_topic","plus"]],null],[1,"\\n"],[13]],[],false,["d-button","concat-class","if"]]',moduleName:"discourse/plugins/discourse-templates/discourse/templates/connectors/topic-above-posts/discourse-templates-button.hbs",isStrictMode:!1})})),define("discourse/plugins/discourse-templates/lib/replace-variables",["exports","discourse/models/user"],(function(e,t){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.TEMPLATES_ALLOWED_VARIABLES=void 0,e.replaceVariables=function(e,o,i){const a=t.default.current(),l={...i||{},my_username:a?.username,my_name:a?.displayName}
if(l&&"object"==typeof l)for(const t of s)l[t]?(e=e.replace(new RegExp(`%{${t}(,fallback:.[^}]*)?}`,"g"),l[t]),o=o.replace(new RegExp(`%{${t}(,fallback:.[^}]*)?}`,"g"),l[t])):(e=(e=e.replace(new RegExp(`%{${t},fallback:(.[^}]*)}`,"g"),"$1")).replace(new RegExp(`%{${t}}`,"g"),""),o=(o=o.replace(new RegExp(`%{${t},fallback:(.[^}]*)}`,"g"),"$1")).replace(new RegExp(`%{${t}}`,"g"),""))
return{title:e,content:o}}
const s=e.TEMPLATES_ALLOWED_VARIABLES=Object.freeze(["my_username","my_name","chat_channel_name","chat_channel_url","chat_thread_name","chat_thread_url","context_title","context_url","topic_title","topic_url","original_poster_username","original_poster_name","reply_to_username","reply_to_name","last_poster_username","reply_to_or_last_poster_username"])})),define("discourse/plugins/discourse-templates/lib/textarea-manipulator",["exports","@ember/application","@ember/object","discourse/mixins/textarea-text-manipulation"],(function(e,t,s,o){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
class i extends(s.default.extend(o.default)){constructor(e,s){super(...arguments),(0,t.setOwner)(this,e),this._textarea=s,this.element=this._textarea,this.ready=!0,this.init()}addBlock(e){this._addBlock(this.getSelected(),e)}}e.default=i})),define("discourse/plugins/discourse-templates/lib/variables-chat-channel",["exports"],(function(e){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=function(e,t,s){if(!e&&!t)return{}
const o=t?.inReplyTo,i={chat_channel_name:e?.title,chat_channel_url:e?.routeModels?s?.urlFor("chat.channel",...e.routeModels):null,reply_to_username:o?.user?.username,reply_to_name:o?.user?.name}
return{...i,context_title:i.chat_channel_name,context_url:i.chat_channel_url}}})),define("discourse/plugins/discourse-templates/lib/variables-chat-thread",["exports","discourse/plugins/discourse-templates/lib/variables-chat-channel"],(function(e,t){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=function(e,s,o){if(!e&&!s)return{}
const i=e?.channel,a=e?.originalMessage,l=(0,t.default)(i,s,o),r={chat_thread_name:e?.title,chat_thread_url:e?.routeModels?o?.urlFor("chat.channel.thread",...e.routeModels):null,reply_to_username:a?.user?.username,reply_to_name:a?.user?.name}
return{...l,...r,context_title:r.chat_thread_name||l.chat_channel_name,context_url:r.chat_thread_url||l.chat_channel_url}}})),define("discourse/plugins/discourse-templates/lib/variables-composer",["exports"],(function(e){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.default=function(e){if(!e)return{}
const t={topic_title:e.topic?.title,topic_url:e.topic?.url,original_poster_username:e.topic?.details.created_by.username,original_poster_name:e.topic?.details.created_by.name,reply_to_username:e.post?.username,reply_to_name:e.post?.name,last_poster_username:e.topic?.last_poster_username,reply_to_or_last_poster_username:e.post?.username||e.topic?.last_poster_username}
return{...t,context_title:t.topic_title,context_url:t.topic_url}}}))

//# sourceMappingURL=discourse-templates-bf4107a4871540d2f7879a2c45e0ef0f05ded352f79344a44769ba6201798f12.map
//!

;
