def mass_adding_companies(record_count=5):
    cmds = {}
    for i in range(record_count):
        req = {
            'cmd_{}'.format(i): {
                'method': 'crm.company.add',
                'params': {
                    'fields': { 'TITLE': 'Ип Ипман {}'.format(i + 1)}
                }
            }
        }
        cmds.update(req)

    h = Bitrix24Hook(domain, hook_code)
    return h.call_batch(cmds)
