window.DjangoNotebookManager = (el, api_url, ipython_server_url) ->
  $ = jQuery

  if api_url[api_url.length-1] != '/'
    api_url = api_url+'/'

  container = Handlebars.templates.djnbmgr_browse({})
  $(el).empty()
  $(el).append(container)


  delete_notebook = (nbid, cb) ->
    params = { 'deleted': true }
    $.ajax {
      type: 'PUT',
      url: api_url+'notebook/'+nbid+'/',
      contentType: 'application/json',
      data: JSON.stringify(params),
      dataType: "json",
      success: ->
        cb(true)
      error: (xhr,textStatus,error) ->
        cb(false)
    }


  refresh = ->
    query = $('.djnbmgr-search').val()

    do ->
      await
        if query != ""
          $.getJSON api_url+'notebook/?order_by=-updated_on&name__icontains='+encodeURIComponent(query), defer r
        else
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
  
  
  find_nb_name = (el) ->
    name = $(el).parents('[data-notebook-id]').first().find('.djnbmgr-notebook-name').text()
    return name


  $('.djnbmgr-notebook-link').live 'click', ->
    nbid = find_nb_id(this)
    window.open(ipython_server_url+'/'+nbid)


  $('.djnbmgr-notebook-delete').live 'click', ->
    nbid = find_nb_id(this)
    if confirm('Delete notebook?')
      await
        delete_notebook nbid, defer r
      if r
        refresh()
      else
        alert 'Cannot delete notebook'


  $('.djnbmgr-notebook-copy').live 'click', ->
    nbid = find_nb_id(this)
    if confirm('Make a copy of this notebook?')
      window.open(ipython_server_url+'/'+nbid+'/copy')
      setTimeout(refresh,1000)


  $('.djnbmgr-notebook-vc').live 'click', ->
    el = this
    nbid = find_nb_id(this)
    name = find_nb_name(this)
    await
      $.getJSON api_url+'archive/?limit=50&order_by=-updated_on&for_notebook_id='+nbid, defer r
    list = Handlebars.templates.djnbmgr_history({ notebooks: r, name: name })
    $(el).parents('td').first().append(list)


  $('.djnbmgr-close').live 'click', ->
    el = this
    $(el).parent('div').remove()


  search_keypress_timeout = 0
  $('.djnbmgr-search').live 'keyup', (e) ->
    clearTimeout(search_keypress_timeout)
    search_keypress_timeout = setTimeout(refresh, 500)


  $('.djnbmgr-notebook-new').live 'click', ->
    window.open(ipython_server_url+'/new')
    setTimeout(refresh,1000)


  refresh()

