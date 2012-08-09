(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['djnbmgr_browse'] = template(function (Handlebars,depth0,helpers,partials,data) {
  helpers = helpers || Handlebars.helpers;
  var foundHelper, self=this;


  return "<div class=\"djnbmgr\">\n\n<div class=\"djnbmgr-left djnbmgr-main\">\n  <div>\n    <h3>Notebooks</h3>\n    <p>\n      <span class=\"djnbmgr-notebook-new\">New Notebook</span>\n    </p>\n    <p>\n      <input type=\"text\" class=\"djnbmgr-search\" value=\"\"\n       placeholder=\"Search notebooks\" />\n    </p>\n    <div class=\"djnbmgr-notebooks\"></div>\n  </div>\n</div>\n\n<div class=\"djnbmgr-left djnbmgr-menu\">\n  <div>\n    <h3>Recently Archived</h3>\n    <div class=\"djnbmgr-archived\"></div>\n    <h3>Recently Trashed</h3>\n    <div class=\"djnbmgr-trashed\"></div>\n  </div>\n</div>\n\n<div class=\"djnbmgr-clear\"></div>\n</div>\n\n";});
templates['djnbmgr_list'] = template(function (Handlebars,depth0,helpers,partials,data) {
  helpers = helpers || Handlebars.helpers;
  var buffer = "", stack1, stack2, foundHelper, tmp1, self=this, functionType="function", helperMissing=helpers.helperMissing, undef=void 0, escapeExpression=this.escapeExpression;

function program1(depth0,data) {
  
  var buffer = "", stack1;
  buffer += "\n  <li>\n    <span class=\"djnbmgr-notebook-name djnbmgr-notebook-link\" data-notebook-id=\"";
  stack1 = depth0.id;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.id", { hash: {} }); }
  buffer += escapeExpression(stack1) + "\">";
  stack1 = depth0.name;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.name", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</span>\n    <span class=\"djnbmgr-notebook-info\">";
  stack1 = depth0.updated_on;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.updated_on", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</span>\n  </li>\n  ";
  return buffer;}

  buffer += "<ul class=\"djnbmgr-notebook-list\">\n  ";
  foundHelper = helpers.notebooks;
  stack1 = foundHelper || depth0.notebooks;
  stack1 = (stack1 === null || stack1 === undefined || stack1 === false ? stack1 : stack1.objects);
  stack2 = helpers.each;
  tmp1 = self.program(1, program1, data);
  tmp1.hash = {};
  tmp1.fn = tmp1;
  tmp1.inverse = self.noop;
  stack1 = stack2.call(depth0, stack1, tmp1);
  if(stack1 || stack1 === 0) { buffer += stack1; }
  buffer += "\n</ul>\n\n";
  return buffer;});
templates['djnbmgr_notebooks'] = template(function (Handlebars,depth0,helpers,partials,data) {
  helpers = helpers || Handlebars.helpers;
  var buffer = "", stack1, stack2, foundHelper, tmp1, self=this, functionType="function", helperMissing=helpers.helperMissing, undef=void 0, escapeExpression=this.escapeExpression;

function program1(depth0,data) {
  
  var buffer = "", stack1;
  buffer += "\n    <tr data-notebook-id=\"";
  stack1 = depth0.id;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.id", { hash: {} }); }
  buffer += escapeExpression(stack1) + "\">\n      <td class=\"djnbmgr-notebook-link\">";
  stack1 = depth0.name;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.name", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</td>\n      <td class=\"djnbmgr-notebook-date\">";
  stack1 = depth0.updated_on;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.updated_on", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</td>\n      <td class=\"djnbmgr-notebook-actions\">\n        <span class=\"djnbmgr-notebook-vc djnbmgr-notebook-action\"\n         >Versions</span> \n        <span class=\"djnbmgr-notebook-copy djnbmgr-notebook-action\"\n         >Copy</span> \n        <span class=\"djnbmgr-notebook-delete djnbmgr-notebook-action\"\n         >Delete</span> \n      </td>\n    </tr>\n  ";
  return buffer;}

  buffer += "<table class=\"djnbmgr-notebook-list\">\n  <tbody>\n  ";
  foundHelper = helpers.notebooks;
  stack1 = foundHelper || depth0.notebooks;
  stack1 = (stack1 === null || stack1 === undefined || stack1 === false ? stack1 : stack1.objects);
  stack2 = helpers.each;
  tmp1 = self.program(1, program1, data);
  tmp1.hash = {};
  tmp1.fn = tmp1;
  tmp1.inverse = self.noop;
  stack1 = stack2.call(depth0, stack1, tmp1);
  if(stack1 || stack1 === 0) { buffer += stack1; }
  buffer += "\n  </tbody>\n</table>\n\n";
  return buffer;});
})();