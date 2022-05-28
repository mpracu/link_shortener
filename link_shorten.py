import pyshorteners

link= "https://www.amazon.de/dp/B084DWG2VQ/ref=gw_de_desk_mso_aucc_brw_bau_xpl2?pf_rd_r=HTCGZEVRYDN8T0T6D742&pf_rd_p=5da74227-0533-497a-bc36-f9385b8377cb&pd_rd_r=81ed1ddb-9f89-444f-b6e4-2c053b232d1e&pd_rd_w=KhnL5&pd_rd_wg=Ji4P8&ref_=pd_gw_unk"

short = pyshorteners.Shortener()
short_link = short.tinyurl.short(link)

print("New link : "+short_link)



