

def parser(input_, subdata,condata):
    import pandas as pd
    import numpy as np
    import zipfile
    #sdf = pd.read_csv('subject_columns.csv', index_col=None)
    cdf = pd.read_excel(condata)
    sdf = pd.read_excel(subdata)
    #input format = f_i_code, branch_code, last_acc_date, date_of_prod,code, corr_flag

    f_i_code = input_[0]
    branch_code = input_[1]
    last_acc_date = input_[2]
    date_of_prod = input_[3]
    code = input_[4]
    corr_flag = input_[5]

    sdf = sdf.fillna(' ')
    cdf = cdf.fillna(' ')

    ####define functions#####
    def zipfiles(x,y):
        output_filename = y
        input_filefolder= x
        with zipfile.ZipFile(output_filename, 'w') as zipF:
            for file in input_filefolder:
                zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
    def insert_col(df,insert_num,col,fill_value):
        df.insert(insert_num, col, fill_value,allow_duplicates=False)
        df[col] = df[col].astype(str)
    #def format_all_dates(df,col_w_dates):
    # i = 0
    # while i < len(col_w_dates): 
        #format_date(df,col_w_dates[i])
        #i += 1
    #title DEFINE INSERT COL AND TO_INT
    #inserts columns at a certain position of it doesnt already exist
    def insert_col(df,insert_num,col,fill_value):
        df.insert(insert_num, col, fill_value)
        df[col] = df[col].astype(str)
        #make all of these columns int. remove the decimal. make this a check
    def to_int(x,df):
        df[[x]] = df[[x]].fillna(0)
        df[[x]] = df[[x]].astype(int)
    #title DEFINE DATE FORMAT, PADDING, AND THEN PAD.
    #sets each column to str then pads accordingly
    def padding_format(df,col,pad_value,fill_char):
        df[col] = df[col].astype(str)
        df[col] = df[col].str.pad(pad_value,side='right',fillchar=fill_char)
        df[col] = df[col].str.slice(0,pad_value)
        
    #title REINDEX COLUMNS IN CORRECT ORDER
    #Inserts Columns in this exact order if it already exist it will keep it but still arrange in order.
    sub_col=['record_type', 'f_i_code', 'branch_code', 'FI Subject Code', 'First Name',
        'Last Name', 'middle_name', 'orig_birth_name', 'orig_birth_surname',
        'mother_maiden_surname', 'title', 'Gender', 'Birthday',
        'place_of_birth', 'country_of_citizenshop_code', 'marital_status',
        'num_of_dependents', 'NIB', 'fffu', 'Street', 'City',
        'addr_p.o.box', 'addr_district', 'addr_country', 'addr_livedSince',
        'add_StreetAddress', 'add_City', 'add_addr_p.o.box',
        'add_addr_district', 'add_addr_country', 'add_addr_livedSince',
        'doc_type', 'doc_num', 'doc_iss_date', 'doc_iss_country',
        'add_doc_type', 'add_doc_nbr', 'add_doc_iss_date',
        'add_doc_iss_country', 'Home Phone', 'Cell Phone',
        'Work Phone', 'Email', 'sole_trade_name',
        'sole_vat_num', 'solTradeBusinessRegNum', 'solTradePlaceOFReg',
        'D_O_Estab', 'solTradePhNum', 'Employer Name', 'occ_status',
        'emp_ph_num', 'date_hired', 'date_terminated', 'occ_type', 'job_title',
        'gross_ann_income', 'prev_emp', 'prev_emp_occ_status', 'prev_emp_phnum',
        'prev_emp_datehired', 'prev_emp_dateterm', 'prev_emp_occ',
        'prev_emp_jobtitle', 'prev_emp_grossannu', 'filler']
    sdf = sdf.reindex(labels=sub_col, axis=1
                    )
    #sdf.reindex(labels=sub_col,axis=1)
    #Inserts Columns in this exact order if it already exist it will keep it but still arrange in order.
    con_col=['record_type', 'f_i_code', 'branch_code', 'FI Subject Code',
    'FI Contract Code', 'Contract_Type', 'Contract_Phase',
    'Contract_Status', 'Currency', 'O_Currency', 'Start Date',
    'Contract_req_date', 'Maturity Date','Contract_end actual date',
    'payment_made_date', 'flag_reorganized_credit',
    'personal_guarantee_type', 'real_guarantee_type',
    'amnt_guaranteed_by_personal_guarantee',
    'amnt_guaranteed_by_real_guarantee', 'max_num_pmnts_pastdue',
    'num_o_months_with_max_overdue', 'max_num_days_pastdue', 'worst_status',
    'date_of_max_insolvency', 'filler', 'Financed Amount','Number of Payments',
    'payment_freq', 'method_of_payment','Monthly Instalment Amount',
    'next_payment_date', 'next_payment_amt','Outstanding Payments Number', 'Outstanding Balance',
    'Num Of Payments past Due', 'Amount Past Due', 'Days past Due',
    'type_of_leased_good', 'value_of_leased_good',
    'new_or_used', 'brand', 'registration_num', 'date_of_manufacturing',
    'real_num_of_days_past_due', 'filler2']
    #'num_of_installments' set to 'number of payments'
    #REINDEX IF NECESSARY
    cdf = cdf.reindex(labels=con_col,axis=1)

    #for all dates replace the '/' with '' and make sure they're strings
    sub_col_w_dates = ['Birthday',
    'addr_livedSince',
    'add_addr_livedSince',
    'doc_iss_date',
    'add_doc_iss_date',
    'date_hired',
    'date_terminated',
    'prev_emp_datehired',
    'prev_emp_dateterm']
    con_col_w_dates = ['Start Date',
                        'Contract_req_date',
                        'Maturity Date',
                        'Contract_end actual date',
                        'payment_made_date',
                        'date_of_max_insolvency',
                        'next_payment_date',
                        'date_of_manufacturing']
    from datetime import datetime


    sdf = sdf.fillna(' ')
    cdf = cdf.fillna(' ') 
    import datetime as dt
    def pad_dates(df,col):
        df[col] = df[col].astype(str)
        df[col] = pd.to_datetime(df[col], format=None, dayfirst=True, errors='ignore')
        df[col] = df[col].astype(str)
        df[col] = df[col].str.pad(8,side='left',fillchar='0')
        df[col] = df[col].str.slice(0,8)

    def pad_all_dates(df,col_w_dates):
        i = 0
        while i < len(col_w_dates): 
            pad_dates(df,col_w_dates[i])
            i += 1

    pad_all_dates(cdf,con_col_w_dates)
    pad_all_dates(sdf,sub_col_w_dates)

    #drop cdf['New Number of Payments'] before export
    cdf['New Number of Payments'] = cdf['Number of Payments'].apply(lambda x: cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due'] if x < x in cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due'] else x)
    cdf.loc[cdf['Number of Payments'].isnull() , 'Number of Payments'] = 0
    to_int('Outstanding Payments Number',cdf)
    cdf['Num Of Payments past Due']=cdf['Num Of Payments past Due'].fillna(0)
    padding_format(cdf,'Num Of Payments past Due',3,'0')

    cdf['Num Of Payments past Due']= pd.to_numeric(cdf['Num Of Payments past Due']).astype(int)

    err_df = cdf.loc[cdf['Number of Payments']<(cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due'])]
    pmts_err = cdf.loc[cdf['Number of Payments']<(cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due']) , 'Number of Payments']
    pmts_fix = cdf.loc[cdf['Number of Payments']<(cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due']) , 'Number of Payments'] = cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due']

    err_df.to_csv('payment_error_file.csv')
    pmts_fix.to_csv('payment_error_fixes.csv')
    cdf.loc[cdf['Number of Payments']<(cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due']) , 'Number of Payments'] = cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due']
    cdf['Number of Payments']=cdf['Number of Payments'].astype(int)

    sdf = sdf.fillna(' ')
    cdf = cdf.fillna(' ')
    sbj_pad_amt = [1,5,8,16,40,40,40,40,40,40, 
    20,1, 8,20,2,1,2,20,13,40,40,30,30,
    2,8,40,40,30,30,2,8,2,20,8,2,2,20,8,
    2,20,20,20,60,120,13,10,30,8,20,
    120,1,20,8,8,3,30,12,120,1,20,8,8,
    3,30,12,54]
    con_pad_amt = [1,5,8,16,35,2,2,1,3,3,8,8,8,8,8,1,3,3,12,12,1,1,1,1,8,159,#general info = 250,
                12,3,1,3,12,8,12,3,12,3,12,1,1,12,1,40,40,8,4,362]#installment contracts = 550, total = 800


    i = 0
    while i < len(sbj_pad_amt): 
        padding_format(sdf,sub_col[i], sbj_pad_amt[i],' ')
        i += 1

    i = 0
    while i < len(con_pad_amt): 
        padding_format(cdf,con_col[i], con_pad_amt[i],' ')
        i += 1

    #title EXPORT PADDED TXT FILE

    sdf['record_type'] ='P'
    cdf['record_type'] ='D'
    sdf['f_i_code'],cdf['f_i_code'] = f_i_code,f_i_code
    sdf['branch_code'],cdf['branch_code'] = branch_code,branch_code

    sdf.to_csv('sdf_padded_complete.txt',header=None,index=None,sep='^')
    cdf.to_csv('cdf_padded_complete.txt',header=None,index=None,sep='^')

    sf = open('sdf_padded_complete.txt')
    sd = sf.read()
    sf.close()
    cf = open('cdf_padded_complete.txt')
    cd = cf.read()
    cf.close()

    sd = sd.replace('^','')
    cd = cd.replace('^','')

    myText = open(r'SubBodyComplete.txt','w')
    myText.write(sd)
    myText.close()
    myText = open(r'ConBodyComplete.txt','w')
    myText.write(cd)
    myText.close()



    #title HEADER FORMAT
    #insert corr_flag for header for contract
    con_head_pad = [1,5,8,8,3,1,774]
    sub_head_pad = [1,5,8,8,3,1475]

    chddata = [['H', f_i_code, last_acc_date, date_of_prod, code,corr_flag,' ']]
    shddata = [['H', f_i_code, last_acc_date, date_of_prod, code,' ']]

    con_head_col = ['Header', 'f_i_code','last_acc_date','date_of_prod','code','corr_flag','filler']
    sub_head_col = ['Header', 'f_i_code','last_acc_date','date_of_prod','code','filler']

    chd = pd.DataFrame(chddata, columns = con_head_col)
    shd = pd.DataFrame(shddata, columns = sub_head_col)

    i = 0
    while i < len(con_head_pad): 
        padding_format(chd,con_head_col[i], con_head_pad[i],' ')
        i += 1

    i = 0
    while i < len(sub_head_pad): 
        padding_format(shd,sub_head_col[i], sub_head_pad[i],' ')
        i += 1


    chd.to_csv('cdhdr.txt',header=None,index=None,sep='^')
    shd.to_csv('sdhdr.txt',header=None,index=None,sep='^')

    f = open('cdhdr.txt')
    chd = f.read()
    f.close()
    f = open('sdhdr.txt')
    shd = f.read()
    f.close()

    chd = chd.replace('^','')
    shd = shd.replace('^','')

    cdText = open(r'con_and_hdr.txt','w')
    cdText.write(chd+cd)
    cdText.close()
    cdText = open(r'sub_and_hdr.txt','w')
    cdText.write(shd+sd)
    cdText.close()
    def n_o_r(df):
        n_o_r = str(len(df))
        return n_o_r

    #title FORMAT FOOTERS

    con_ftr_pad=[1,5,8,8,7,771]
    sub_ftr_pad=[1,5,8,8,7,1471]

    fddata = [['Q', f_i_code, last_acc_date, date_of_prod, 0, '']]
    fcol = ['Footer', 'f_i_code','last_acc_date','date_of_prod','num_of_records','filler']

    sfd = pd.DataFrame(fddata, columns = fcol )
    cfd = pd.DataFrame(fddata, columns = fcol )

    sfd['num_of_records'] = n_o_r(sdf)
    cfd['num_of_records'] = n_o_r(cdf)

    i = 0
    while i < len(con_ftr_pad): 
        padding_format(cfd,fcol[i], con_ftr_pad[i],' ')
        i += 1

    i = 0
    while i < len(sub_ftr_pad): 
        padding_format(sfd,fcol[i], sub_ftr_pad[i],' ')
        i += 1

    sfd.to_csv('sub_ftr_data.txt',header=None,index=None,sep='^')
    cfd.to_csv('con_ftr_data.txt',header=None,index=None,sep='^')

    ft = open('sub_ftr_data.txt')
    sfd = ft.read()
    f.close()
    ft = open('con_ftr_data.txt')
    cfd = ft.read()
    f.close()

    #title .txt FORMAT
    sfd = sfd.replace('^','')
    cfd = cfd.replace('^','')

    sub_filename = f_i_code+'SJF.txt'
    con_filename = f_i_code+'CNF.txt'

    sdText = open(sub_filename,'w')
    sdText.write(shd+sd+sfd)
    sdText.close()

    sdText = open(con_filename,'w')
    sdText.write(chd+cd+cfd)
    sdText.close()
    #title ZIP FILES
    date_and_code = str(date_of_prod +'_'+f_i_code+'.zip')
    dnc = str(date_of_prod+'_'+f_i_code)
    zfiles = (sub_filename,con_filename)
    zipfiles(zfiles, date_and_code)
