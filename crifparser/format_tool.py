import pandas as pd
import numpy as np
import datetime as dt

def parser(input_,SUBJECT_FILE,CONTRACT_FILE):
    import pandas as pd
    import numpy as np
    import datetime as dt
    today = dt.date.today()
    filedate = today.strftime("%Y%m%d")
    today = today.strftime("%d%m%Y")

    f_i_code = input_[0]
    branch_code = input_[1]
    last_acc_date = input_[2]
    code = input_[3]
    corr_flag = input_[4]

    date_of_prod = today 

    #input = f_i_code, branch_code, last_acc_date, code, corr_flag
    #title READ IN CSV FILE, PAD AMT FOR SUB AN CON DF.

    #PADDING AMOUNTS FOR SUBJECT AND CONTRACT IN ORDER.
    sbj_pad_amt = [1,5,8,16,40,40,40,40,40,40, 
    20,1, 8,20,2,1,2,20,13,40,40,30,30,
    2,8,40,40,30,30,2,8,2,20,8,2,2,20,8,
    2,20,20,20,60,120,13,10,30,8,20,
    120,1,20,8,8,3,30,12,120,1,20,8,8,
    3,30,12,54]
    con_pad_amt = [1,5,8,16,35,2,2,1,3,3,8,8,8,8,8,1,3,3,12,12,1,1,1,1,8,91,#general info = 250,
                12,3,1,3,12,8,12,3,12,3,12,1,1,12,1,40,40,8,4,362]#installment contracts = 550, total = 800

    cdf = pd.read_excel(CONTRACT_FILE)
    sdf = pd.read_excel(SUBJECT_FILE)


    sdf = sdf.fillna(' ')
    cdf = cdf.fillna(' ')

    #SETTING PARAMS FOR FOLING VARIABLES
    sdf[['record_type','f_i_code', 'branch_code']]= 'P',f_i_code,branch_code
    cdf[['record_type','f_i_code', 'branch_code']]= 'D',f_i_code,branch_code
    cdf[['Currency','payment_freq','Contract_Type', 'Contract_Phase']]='BSD','M','14','LV'


    #title DEFINE INSERT COL AND TO_INT
    #inserts columns at a certain position of it doesnt already exist
    def insert_col(df,insert_num,col,fill_value):
        df.insert(insert_num, col, fill_value,allow_duplicates=False)
        df[col] = df[col].astype(str)
    #make all of these columns int. remove the decimal. make this a check
    def to_int(x,df):
        df[[x]] = df[[x]].fillna(0)
        df[[x]] = df[[x]].astype(int)
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
    #REINDEX ADDS THE COLUMNS IF IT ISNT ALREADY THERE 
    #BUT IT DELETES AND COLUMNS THAT ISNT LISTED.
    cdf = cdf.reindex(labels=con_col,axis=1)

    #title DEFINE DATE FORMAT, PADDING, AND THEN PAD.
    #sets each column to str then pads accordingly
    def padding_format(df,col,pad_value,fill_char):
        df[col] = df[col].astype(str)
        df[col] = df[col].str.pad(pad_value,side='right',fillchar=fill_char)
        df[col] = df[col].str.slice(0,pad_value)

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

    #THE FILE BEFORE PARSING. BUT WITH THE COLUMN NAMES AND ORDER.
    sdf.to_excel('C:/Users/Juniqua/Desktop/crif/downloads/CRIFSUBJECTDATA_BPARSING.xlsx',index=None)
    cdf.to_excel('C:/Users/Juniqua/Desktop/crif/downloads/CRIFCONTRACTDATA_BPARSING.xlsx',index=None)

    #THE CODE HERE IS FOR CALCULATING THE TOTAL NUM OF PMTS IN THE DF
    #IN AN UPDATED VERSION I WILL MAKE THIS A FUNCTION YOU CAN CALL
    #SO THIS CAN BE A A FEATURE.
    cdf['Num Of Payments past Due']= cdf['Num Of Payments past Due'].astype(str).apply(lambda x: x.replace('.0',''))
    cdf['Outstanding Payments Number']= cdf['Outstanding Payments Number'].astype(str).apply(lambda x: x.replace('.0',''))
    cdf['Number of Payments']= cdf['Number of Payments'].astype(str).apply(lambda x: x.replace('.0',''))

    #cdf['New Number of Payments'] HAS BEEN ADDED TO THE DF, BUT WILL DELETE before export
    cdf['New Number of Payments'] = cdf['Number of Payments'].apply(lambda x: cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due'] if x < x in cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due'] else x)
    cdf.loc[cdf['Number of Payments'].isnull() , 'Number of Payments'] = 0

    cdf['Num Of Payments past Due']=cdf['Num Of Payments past Due'].fillna(0)

    cdf['Num Of Payments past Due'] = cdf['Num Of Payments past Due'].astype(str)
    cdf['Num Of Payments past Due'] = cdf['Num Of Payments past Due'].str.pad(3,side='left',fillchar='0')
    cdf['Num Of Payments past Due'] = cdf['Num Of Payments past Due'].str.slice(0,3)

    cdf['Outstanding Payments Number'] = cdf['Outstanding Payments Number'].str.pad(3,side='left',fillchar='0')
    cdf['Outstanding Payments Number'] = cdf['Outstanding Payments Number'].str.slice(0,3)
    cdf['Outstanding Payments Number']=cdf['Outstanding Payments Number'].fillna(0)
    cdf['Outstanding Payments Number'] = cdf['Outstanding Payments Number'].astype(str)

    cdf['Number of Payments'] = cdf['Number of Payments'].str.pad(3,side='left',fillchar='0')
    cdf['Number of Payments'] = cdf['Number of Payments'].str.slice(0,3)
    cdf['Number of Payments']=cdf['Number of Payments'].fillna(0)
    cdf['Number of Payments'] = cdf['Number of Payments'].astype(str)

    cdf['Num Of Payments past Due']= cdf['Num Of Payments past Due'].map(lambda x: int(x.replace(' ',''))).astype(int)
    cdf['Outstanding Payments Number']= cdf['Outstanding Payments Number'].map(lambda x: int(x.replace(' ',''))).astype(int)
    cdf['Number of Payments']= cdf['Number of Payments'].map(lambda x: int(x.replace(' ',''))).astype(int)

    #error files before export
    #err_df = cdf.loc[cdf['Number of Payments']<(cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due'])]
    #pmts_err = cdf.loc[cdf['Number of Payments']<(cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due']) , 'Number of Payments']
    #pmts_fix = cdf.loc[cdf['Number of Payments']<(cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due']) , 'Number of Payments'] = cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due']

    #SENDS THE ERRORS DATAFRAME TO AN EXCEL TO VIEW THE PERSONAL FILES THAT NEED CORRECTION
    #err_df.to_excel('C://Users//Juniqua//Desktop//crif//downloads//payment_error_file.xlsx')
    #SENDS A LIST OF THE NEW PAYMENTS NUMBERS, CORRESPONDS LINE FOR LINE ON 'ERR_DF' FILE
    #pmts_fix.to_excel('C://Users//Juniqua//Desktop//crif//downloads//payment_error_fixes.xlsx')

    #THIS PORTION LOCATES THE ERRORS IN THE DF AND SETS THE 'NEW NUM OF PMTS' TO 'NUM OF PMTS'
    cdf.loc[cdf['Number of Payments']<(cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due']) , 'Number of Payments'] = cdf['Outstanding Payments Number']+cdf['Num Of Payments past Due']
    cdf['Number of Payments']=cdf['Number of Payments'].astype(int)
    #duplicate start date and maturity date to contract req dat and contract actual end date
    cdf['Contract_req_date']=cdf['Start Date']
    cdf['Contract_end actual date'] = cdf['Maturity Date']
    #cdf['Maturity Date'] = pd.to_datetime(cdf['Maturity Date'])
    #cdf['Start Date'] = pd.to_datetime(cdf['Start Date'])
    cdf[['Maturity Date','Start Date']] = cdf[['Maturity Date','Start Date']].astype(str)

    #THIS FUNCTION PADS ALL THE NUMERICAL FIELDS
    def pad_num(df,col,pad_value,fill_char):
        df[col] = df[col].astype(str)
        df[col] = df[col].str.split(pat='.',expand=True)[0]
        df[col] = df[col].astype(str).apply(lambda x: x.replace(' ',''))
        df[col] = df[col].str.pad(pad_value,side='left',fillchar=fill_char)
        df[col] = df[col].str.slice(0,pad_value)

    #ANY FIELDS ADDED TO THIS LIST HAS TO BE A NUMERICAL FIELD. **DATES NOT INCLUDED**
    numerical_fields = ['amnt_guaranteed_by_personal_guarantee', 'amnt_guaranteed_by_real_guarantee', 'max_num_pmnts_pastdue',
    'num_o_months_with_max_overdue', 'max_num_days_pastdue','Financed Amount','Number of Payments',
    'Monthly Instalment Amount', 'Outstanding Payments Number', 'Outstanding Balance',
    'Num Of Payments past Due', 'Amount Past Due', 'value_of_leased_good','registration_num',
    'real_num_of_days_past_due','next_payment_amt','num_o_months_with_max_overdue', 'max_num_days_pastdue', ]

    #THIS LOOP GOES THROUGH THE ABOVE LIST OF NUMERICAL FIELDS AND FINDS THEM IN THE DF
    #ONCE THE POSITION IS FOUND ITS ADDED TO A LIST FOR THE FINAL LOOP.
    i=0
    ax = []
    while i < len(numerical_fields):
        ix = con_col.index(numerical_fields[i])
        i+=1
        ax.append(ix)

    #THIS LOOP USES THE ABOVE LIST TO FIND THE CORRECT PADDING AMOUNT
    i=0
    pa = []
    while i < len(ax):
        ix = con_pad_amt[ax[i]]
        i+=1
        pa.append(ix)

    #THIS IS THE FINAL LOOP. GOES THROUGH BOTH OF THE ABOVE LISTS TO CORRECTLY PAD 
    #EACH COLUMN, AND FILL WITH ZEROS TO THE LEFT.
    i=0
    while i < len(numerical_fields):
        pad_num(cdf, numerical_fields[i],pa[i],'0')
        i+=1
    #**THIS FUNCTION IS FOR DATES ONLY!**
    #SPECIAL NOTE IF THE DATE IS NOT IN THE CORRECT FORMAT IT WILL BE SET AS
    #'NAT' MEANING 'NOT A TIME'
    #OR SET AS 'NAN' FOR 'NOT A NUMBER'
    #ANYTHING EXCEEDING WILL BE SLICED OFF.
    import datetime as dt
    def pad_dates(df,col):
        df[col] = df[col].astype(str)
        df[col] = pd.to_datetime(df[col], format=None, errors='coerce')
        df[col] = df[col].dt.strftime('%d%m%Y')
        df[col] = df[col].fillna('0')
        df[col] = df[col].astype(str)
        df[col] = df[col].str.pad(8,side='left',fillchar='0')
        df[col] = df[col].str.slice(0,8)

    #THIS FUNCTION GOES THROUGH THE LIST OF COLUMNS WITH DATES ALREADY SET IN THE
    #VARIABLES AT THE BEGINNNING.
    def pad_all_dates(df,col_w_dates):
        i = 0
        while i < len(col_w_dates): 
            pad_dates(df,col_w_dates[i])
            i += 1
    #CALLS TEH FUNCTION TO PAD ALL DATES
    pad_all_dates(cdf,con_col_w_dates)
    pad_all_dates(sdf,sub_col_w_dates)
    sdf = sdf.fillna(' ')
    cdf = cdf.fillna(' ')

    # THIS LOOP pads all fields IN BOTH SUBJECT AN CONTRACT DF'S
    i = 0
    while i < len(sbj_pad_amt): 
        padding_format(sdf,sub_col[i], sbj_pad_amt[i],' ')
        i += 1

    i = 0

    while i < len(con_pad_amt): 
        padding_format(cdf,con_col[i], con_pad_amt[i],' ')
        i += 1

    #THIS MAKES SURE THE COLUMNS ARE STILL IN THE CORRECT ORDER BEFORE ANY FURTHER FORMATTING
    cdf = cdf.reindex(labels=con_col,axis=1)
    sdf = sdf.reindex(labels=sub_col, axis=1)
    #SETS THE DATES TO EQUAL THE ORIGINAL START AND MATURITY DATES. THIS WILL ALSO BE
    #A CONDITIONAL LOOP UST INCASE FUTURE CLIENTS HAVE THIS INFORMATION ALREADY
    cdf['Contract_req_date'] = cdf['Start Date']
    cdf['Contract_end actual date'] = cdf['Maturity Date']

    #DROPS THE UNNECESSARY COLUMNS BEFORE CONVERTING TO .TXT FILE
    cdf = cdf.drop(['filler2'],axis=1)
    sdf = sdf.drop(['filler'],axis=1)

    #title EXPORT PADDED TXT FILE
    #SETS THE NECESSARY VARIABLES

    sdf['record_type'] ='P'
    cdf['record_type'] ='D'
    sdf['f_i_code'],cdf['f_i_code'] = f_i_code,f_i_code
    sdf['branch_code'],cdf['branch_code'] = branch_code,branch_code

    #SENDS THE FILE OUT WITH A UNIQUE SPLITTING CHARACTER '^'
    sdf.to_csv('C:/Users/Juniqua/Desktop/crif/downloads/sdf_padded_complete.txt',header=None,index=None,sep='^')
    cdf.to_csv('C:/Users/Juniqua/Desktop/crif/downloads/cdf_padded_complete.txt',header=None,index=None,sep='^')

    #BRINGS THAT SAME FILE BACK IN
    sf = open('C:/Users/Juniqua/Desktop/crif/downloads/sdf_padded_complete.txt')
    sd = sf.read()
    sf.close()
    cf = open('C:/Users/Juniqua/Desktop/crif/downloads/cdf_padded_complete.txt')
    cd = cf.read()
    cf.close()

    #REMOVES THE SPECIAL CHAR 
    sd = sd.replace('^','')
    cd = cd.replace('^','')

    #CREATING THE BODY .TXT FILE
    myText = open(r'C:/Users/Juniqua/Desktop/crif/downloads/SubBodyComplete.txt','w')
    myText.write(sd)
    myText.close()
    myText = open(r'C:/Users/Juniqua/Desktop/crif/downloads/ConBodyComplete.txt','w')
    myText.write(cd)
    myText.close()

    # Header format
    #title HEADER FORMAT
    #insert corr_flag for header for contract
    #CREATES HEADER
    con_head_pad = [1,5,8,8,3,1,0]#FILLER = 774
    sub_head_pad = [1,5,8,8,3,0]#FILLER = 1475

    chddata = [['H', f_i_code, last_acc_date, date_of_prod, code,corr_flag,' ']]
    shddata = [['H', f_i_code, last_acc_date, date_of_prod, code,' ']]

    con_head_col = ['Header', 'f_i_code','last_acc_date','date_of_prod','code','corr_flag','filler']
    sub_head_col = ['Header', 'f_i_code','last_acc_date','date_of_prod','code','filler']

    chd = pd.DataFrame(chddata, columns = con_head_col)
    shd = pd.DataFrame(shddata, columns = sub_head_col)
    #PADS HEADER
    i = 0
    while i < len(con_head_pad): 
        padding_format(chd,con_head_col[i], con_head_pad[i],' ')
        i += 1

    i = 0
    while i < len(sub_head_pad): 
        padding_format(shd,sub_head_col[i], sub_head_pad[i],' ')
        i += 1


    chd.to_csv('C:/Users/Juniqua/Desktop/crif/downloads/cdhdr.txt',header=None,index=None,sep='^')
    shd.to_csv('C:/Users/Juniqua/Desktop/crif/downloads/sdhdr.txt',header=None,index=None,sep='^')

    f = open('C:/Users/Juniqua/Desktop/crif/downloads/cdhdr.txt')
    chd = f.read()
    f.close()
    f = open('C:/Users/Juniqua/Desktop/crif/downloads/sdhdr.txt')
    shd = f.read()
    f.close()

    chd = chd.replace('^','')
    shd = shd.replace('^','')

    cdText = open(r'C:/Users/Juniqua/Desktop/crif/downloads/con_and_hdr.txt','w')
    cdText.write(chd+cd)
    cdText.close()
    cdText = open(r'C:/Users/Juniqua/Desktop/crif/downloads/sub_and_hdr.txt','w')
    cdText.write(shd+sd)
    cdText.close()
    # Footer format
    #THIS FUNCTION IS FOR THE NUMBER OF RECORDS
    def n_o_r(df):
        n_o_r = str(len(df))
        return n_o_r

    #title FORMAT FOOTERS
    #CREATES THE FOOTER
    con_ftr_pad=[1,5,8,8,7,0]# FILLER VALUE = 771
    sub_ftr_pad=[1,5,8,8,7,0]#FILLER VALUE = 1471

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

    sfd.to_csv('C:/Users/Juniqua/Desktop/crif/downloads/sub_ftr_data.txt',header=None,index=None,sep='^')
    cfd.to_csv('C:/Users/Juniqua/Desktop/crif/downloads/con_ftr_data.txt',header=None,index=None,sep='^')

    ft = open('C:/Users/Juniqua/Desktop/crif/downloads/sub_ftr_data.txt')
    sfd = ft.read()
    f.close()
    ft = open('C:/Users/Juniqua/Desktop/crif/downloads/con_ftr_data.txt')
    cfd = ft.read()
    f.close()

    # Export format as .txt type
    #title .txt FORMAT
    #JOINS THE .TXT FILES TO CREATE FINAL FILE
    sfd = sfd.replace('^','')
    cfd = cfd.replace('^','')

    sub_filename = 'C:/Users/Juniqua/Desktop/crif/downloads/'+f_i_code+'SJF.txt'
    con_filename = 'C:/Users/Juniqua/Desktop/crif/downloads/'+f_i_code+'CNF.txt'

    sdText = open(sub_filename,'w')
    sdText.write(shd+sd+sfd)
    sdText.close()

    sdText = open(con_filename,'w')
    sdText.write(chd+cd+cfd)
    sdText.close()
    # Compress into Zip
    #title DEFINED ZIP
    import zipfile

    #THIS FUNCTION IS FOR ZIPPING THE FILES
    def zipfiles(x,y):
        output_filename = y
        input_filefolder= x
        with zipfile.ZipFile(output_filename, 'w') as zipF:
            for file in input_filefolder:
                zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)

    #title ZIP FILES
    #SETS THE FILE TO THE COMPANY'S INPUT NAME AND THE FILE DATE PROVIDED AT THE BEGINNING

    download_location =  "C:/Users/Juniqua/Desktop/crif/downloads/"
    date_and_code = str(download_location + filedate +'_'+ f_i_code+'.zip') 
    
    #dnc = str(date_of_prod+'_'+f_i_code)
    zfiles = (sub_filename,con_filename)
    zipfiles(zfiles, date_and_code)
