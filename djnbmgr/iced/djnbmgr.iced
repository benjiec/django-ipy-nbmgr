window.DjangoNotebookManager = (el, api_url_base, ipython_server_url) ->

  $ = jQuery

  if api_url_base[api_url_base.length-1] != '/'
    api_url_base = api_url_base+'/'

  $('.notebook-link').live 'click', ->
    nbid = $(this).data('notebook-id')
    window.open(ipython_server_url+'/'+nbid)

  await
    $.getJSON api_url_base+'notebook/?order_by=-updated_on', defer notebooks
    $.getJSON api_url_base+'archive/?limit=10&order_by=-updated_on', defer archives
    $.getJSON api_url_base+'trashed/?order_by=-updated_on', defer trash

  container = Handlebars.templates.djnbmgr_browse({
    notebooks: notebooks,
    archives: archives,
    trash: trash
  })

  $(el).empty()
  $(el).append(container)


