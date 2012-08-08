(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['djnbmgr_browse'] = template(function (Handlebars,depth0,helpers,partials,data) {
  helpers = helpers || Handlebars.helpers;
  var buffer = "", stack1, stack2, foundHelper, tmp1, self=this, functionType="function", helperMissing=helpers.helperMissing, undef=void 0, escapeExpression=this.escapeExpression;

function program1(depth0,data) {
  
  var buffer = "", stack1;
  buffer += "\n  <li class=\"notebook-link\" data-notebook-id=\"";
  stack1 = depth0.id;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.id", { hash: {} }); }
  buffer += escapeExpression(stack1) + "\">\n    <span class=\"name\">";
  stack1 = depth0.name;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.name", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</span><br/>\n    <span class=\"date\">Updated: ";
  stack1 = depth0.updated_on;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.updated_on", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</span>\n    <span class=\"date\">Created: ";
  stack1 = depth0.created_on;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.created_on", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</span>\n  </li>\n  ";
  return buffer;}

function program3(depth0,data) {
  
  var buffer = "", stack1;
  buffer += "\n  <li class=\"notebook-link\" data-notebook-id=\"";
  stack1 = depth0.id;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.id", { hash: {} }); }
  buffer += escapeExpression(stack1) + "\">\n    <span class=\"name\">";
  stack1 = depth0.name;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.name", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</span><br/>\n    <span class=\"date\">Updated: ";
  stack1 = depth0.updated_on;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.updated_on", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</span>\n    <span class=\"date\">Created: ";
  stack1 = depth0.created_on;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.created_on", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</span>\n  </li>\n  ";
  return buffer;}

function program5(depth0,data) {
  
  var buffer = "", stack1;
  buffer += "\n  <li class=\"notebook-link\" data-notebook-id=\"";
  stack1 = depth0.id;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.id", { hash: {} }); }
  buffer += escapeExpression(stack1) + "\">\n    <span class=\"name\">";
  stack1 = depth0.name;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.name", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</span><br/>\n    <span class=\"date\">Updated: ";
  stack1 = depth0.updated_on;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.updated_on", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</span>\n    <span class=\"date\">Created: ";
  stack1 = depth0.created_on;
  if(typeof stack1 === functionType) { stack1 = stack1.call(depth0, { hash: {} }); }
  else if(stack1=== undef) { stack1 = helperMissing.call(depth0, "this.created_on", { hash: {} }); }
  buffer += escapeExpression(stack1) + "</span>\n  </li>\n  ";
  return buffer;}

  buffer += "<h3>Notebooks</h3>\n<ul>\n  ";
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
  buffer += "\n</ul>\n\n\n<h3>Archives</h3>\n<ul>\n  ";
  foundHelper = helpers.archives;
  stack1 = foundHelper || depth0.archives;
  stack1 = (stack1 === null || stack1 === undefined || stack1 === false ? stack1 : stack1.objects);
  stack2 = helpers.each;
  tmp1 = self.program(3, program3, data);
  tmp1.hash = {};
  tmp1.fn = tmp1;
  tmp1.inverse = self.noop;
  stack1 = stack2.call(depth0, stack1, tmp1);
  if(stack1 || stack1 === 0) { buffer += stack1; }
  buffer += "\n</ul>\n\n\n<h3>Trash</h3>\n<ul>\n  ";
  foundHelper = helpers.trash;
  stack1 = foundHelper || depth0.trash;
  stack1 = (stack1 === null || stack1 === undefined || stack1 === false ? stack1 : stack1.objects);
  stack2 = helpers.each;
  tmp1 = self.program(5, program5, data);
  tmp1.hash = {};
  tmp1.fn = tmp1;
  tmp1.inverse = self.noop;
  stack1 = stack2.call(depth0, stack1, tmp1);
  if(stack1 || stack1 === 0) { buffer += stack1; }
  buffer += "\n</ul>\n\n";
  return buffer;});
})();