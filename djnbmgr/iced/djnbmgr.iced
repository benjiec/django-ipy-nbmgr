window.DjangoNotebookManager = (el, api_url, ipython_server_url) ->
  $ = jQuery

  if api_url[api_url.length-1] != '/'
    api_url = api_url+'/'

  container = Handlebars.templates.djnbmgr_browse({})
  $(el).empty()
  $(el).append(container)

  refresh = ->
    do ->
      await
        $.getJSON api_url+'notebook/?order_by=-updated_on', defer r
      list = Handlebars.templates.djnbmgr_notebooks({ notebooks: r })
      $('.djnbmgr-notebooks',el).empty().append(list)

    do ->
      await
        $.getJSON api_url+'archive/?limit=10&order_by=-updated_on', defer r
      list = Handlebars.templates.djnbmgr_list({ notebooks: r })
      $('.djnbmgr-archived',el).empty().append(list)

    do ->
      await
        $.getJSON api_url+'trashed/?limit=10&order_by=-updated_on', defer r
      list = Handlebars.templates.djnbmgr_list({ notebooks: r })
      $('.djnbmgr-trashed',el).empty().append(list)

  find_nb_id = (el) ->
    nbid = $(el).parents('[data-notebook-id]').first().data('notebook-id')
    return nbid

  $('.djnbmgr-notebook-link').live 'click', ->
    nbid = find_nb_id(this)
    window.open(ipython_server_url+'/'+nbid)

  $('.djnbmgr-notebook-delete').live 'click', ->
    nbid = find_nb_id(this)
    alert "delete "+nbid
    refresh()

  $('.djnbmgr-notebook-copy').live 'click', ->
    nbid = find_nb_id(this)
    alert "copy "+nbid
    refresh()

  $('.djnbmgr-notebook-vc').live 'click', ->
    nbid = find_nb_id(this)
    alert "vc "+nbid
  
  $('.djnbmgr-search').live 'keypress', (e) ->
    if e.which == 13
      query = $(this).val()
      alert "search "+query

  $('.djnbmgr-notebook-new').live 'click', ->
    window.open(ipython_server_url+'/new')
    refresh()
  
  refresh()

