from hh import get_max_page,get_hh_jobs
from save import save_to_csv
from db import data_base

def parsing(): 
    max_page = get_max_page() 
    jobs = get_hh_jobs(max_page)
    save_to_csv(jobs)
    data_base(jobs)

