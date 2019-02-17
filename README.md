# dropbox2csv

This is a kit for converting dropbox xlsx file to csv 

`
r = dropbox2csv.get('/path_to_folder/',token="",'.xlsx')
`

`
r.to_xlsx('/local_folder/')
r.to_csv('/local_folder/')
r.to_pickle('/local_folder/')
r.to_list()
df = r.to_df()
`


