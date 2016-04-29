#!/usr/bin/env python

from wmflabs import db

#Connect to db
conn = db.connect('wikidatawiki')
#Fetch data
cur = conn.cursor()
with cur:
	sql = 'select ips_item_id, ips_site_page from wb_items_per_site where ips_site_id="cswiki" and ips_site_page in (select page_title from cswiki_p.page where page_id in (select cl_from from cswiki_p.categorylinks where cl_to="Údržba:Doplnit_štítek_na_Wikidatech"))'
	cur.execute(sql)
	data = cur.fetchall()

