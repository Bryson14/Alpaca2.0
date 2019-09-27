#! /usr/bin/python3.6

import sys
import requests
import pandas as pd
from pathlib2 import Path


class StockBatch:
	def __init__(self):
		self.batches = ['MMM,ABT,ABBV,ABMD,ACN,ATVI,ADBE,AMD,AAP,AES,AET,AMG,AFL,A,APD,AKAM,ALK,ALB,ARE,ALXN,ALGN,ALLE,AGN,ADS,LNT,ALL,GOOGL,GOOG,MO,AMZN,AEE,AAL,AEP,AXP,AIG,AMT,AWK,AMP,ABC,AME,AMGN,APH,APC,ADI,ANSS,ANTM,AON,AOS,APA,AIV,AAPL,AMAT,APTV,ADM,ARNC,ANET,AJG,AIZ,T,ADSK,ADP,AZO,AVB,AVY,BHGE,BLL,BAC,BK,BAX,BBT,BDX,BRK-B,BBY,BIIB,BLK,HRB,BA,BKNG,BWA,BXP,BSX,BHF,BMY,AVGO,BR,BF-B,CHRW,COG,CDNS,CPB,COF,CAH,KMX,CCL,CAT,CBOE,CBRE,CBS,CELG&',
			'CNC,CNP,CTL,CERN,CF,SCHW,CHTR,CVX,CMG,CB,CHD,CI,XEC,CINF,CTAS,CSCO,C,CFG,CTXS,CLX,CME,CMS,KO,CTSH,CL,CMCSA,CMA,CAG,CXO,COP,ED,STZ,COO,CPRT,GLW,COST,COTY,CCI,CSX,CMI,CVS,DHI,DHR,DRI,DVA,DE,DAL,XRAY,DVN,DLR,DFS,DISCA,DISCK,DISH,DG,DLTR,D,DOV,DWDP,DTE,DRE,DUK,DXC,ETFC,EMN,ETN,EBAY,ECL,EIX,EW,EA,EMR,ETR,EOG,EFX,EQIX,EQR,ESS,EL,EVRG,ES,RE,EXC,EXPE,EXPD,ESRX,EXR,XOM,FFIV,FB,FAST,FRT,FDX,FIS,FITB,FE,FISV,FLT,FLIR,FLS&',
			'FLR,FMC,FL,F,FTNT,FTV,FBHS,BEN,FCX,GPS,GRMN,IT,GD,GE,GIS,GM,GPC,GILD,GPN,GS,GT,GWW,HAL,HBI,HOG,HRS,HIG,HAS,HCA,HCP,HP,HSIC,HSY,HES,HPE,HLT,HFC,HOLX,HD,HON,HRL,HST,HPQ,HUM,HBAN,HII,IDXX,INFO,ITW,ILMN,IR,INTC,ICE,IBM,INCY,IP,IPG,IFF,INTU,ISRG,IVZ,IPGP,IQV,IRM,JKHY,JEC,JBHT,JEF,SJM,JNJ,JCI,JPM,JNPR,KSU,K,KEY,KEYS,KMB,KIM,KMI,KLAC,KSS,KHC,KR,LB,LLL,LH,LRCX,LEG,LEN,LLY,LNC,LIN,LKQ,LMT,L,LOW,LYB,MTB,MAC&',
			'M,MRO,MPC,MAR,MMC,MLM,MAS,MA,MAT,MKC,MCD,MCK,MDT,MRK,MET,MTD,MGM,KORS,MCHP,MU,MSFT,MAA,MHK,TAP,MDLZ,MNST,MCO,MS,MOS,MSI,MSCI,MYL,NDAQ,NOV,NKTR,NTAP,NFLX,NWL,NFX,NEM,NWSA,NWS,NEE,NLSN,NKE,NI,NBL,JWN,NSC,NTRS,NOC,NCLH,NRG,NUE,NVDA,ORLY,OXY,OMC,OKE,ORCL,PCAR,PKG,PH,PAYX,PYPL,PNR,PBCT,PEP,PKI,PRGO,PFE,PCG,PM,PSX,PNW,PXD,PNC,RL,PPG,PPL,PFG,PG,PGR,PLD,PRU,PEG,PSA,PHM,PVH,QRVO,PWR,QCOM,DGX,RJF,RTN,O,RHT,REG,REGN,RF&',
			'RSG,RMD,RHI,ROK,COL,ROL,ROP,ROST,RCL,CRM,SBAC,SCG,SLB,STX,SEE,SRE,SHW,SPG,SWKS,SLG,SNA,SO,LUV,SPGI,SWK,SBUX,STT,SRCL,SYK,STI,SIVB,SYMC,SYF,SNPS,SYY,TROW,TTWO,TPR,TGT,TEL,FTI,TXN,TXT,TMO,TIF,TWTR,TJX,TMK,TSS,TSCO,TDG,TRV,TRIP,FOXA,FOX,TSN,UDR,ULTA,USB,UAA,UA,UNP,UAL,UNH,UPS,URI,UTX,UHS,UNM,VFC,VLO,VAR,VTR,VRSN,VRSK,VZ,VRTX,VIAB,V,VNO,VMC,WMT,WBA,DIS,WM,WAT,WEC,WCG,WFC,WELL,WDC,WU,WRK,WY,WHR,WMB,WLTW,WYNN,XEL,XRX&',
			'XLNX,XYL,YUM,ZBH,ZION,ZTS,QQQ,SQQQ,SPY&']
		
	def map_to_df(self, df, stockname, day):
		date = open_val = close = high = low = vol = change = change_percent = vwap = None
		
		if 'date' in df.keys():
			date = day['date']
		if 'open' in df.keys():
			open_val = day['open']
		if 'close' in df.keys():
			close = day['close']
		if 'high' in df.keys():
			high = day['high']
		if 'low' in df.keys():
			low = day['low']
		if 'volume' in df.keys():
			vol = day['volume']
		if 'change' in df.keys():
			change = day['change']
		if 'changePercent' in df.keys():
			change_percent = day['changePercent']
		if ' vwap' in df.keys():
			vwap = day['vwap']
		
		df = df.append({
			'date': date,
			'symbol': stockname,
			'open': open_val,
			'close': close,
			'high': high,
			'low': low,
			'vol': vol,
			'change': change,
			'changePercent': change_percent,
			'vwap': vwap
		}, ignore_index=True)
		return df
		
	def download(self, required_option, other_option):
		path_to_dir = Path.joinpath(Path.cwd(), 'Data', 'StockData')
		columns = ['date', 'symbol', 'open', 'high', 'low', 'close', 'volume', 'change', 'changePercent', 'vwap']
		if not other_option:
			for batch in self.batches:
				json = self.get_batch(batch, required_option)
				for stock_name in json:
					print('\t' + stock_name)
					
					try:
						df = pd.read_csv(Path.joinpath(path_to_dir, (stock_name + '.csv')))
					except IOError:
						df = pd.DataFrame(columns=columns)
					for day in json[stock_name]['chart']:
						if day['date'] in df.date.values:
							pass
						else:
							df = self.map_to_df(df, stock_name, day)
					df = df.sort_values('date')
					df.to_csv(Path.joinpath(path_to_dir, (stock_name + '.csv')), index=False)
					
		else:
			json = self.get_batch(required_option, other_option)
			print(json)
			sys.exit(1)
		
	def get_batch(self, symbols, window):
		base_url = 'https://api.iextrading.com/1.0/stock/'
		if ',' in symbols:
			data = requests.get(base_url + 'market/batch?symbols='+symbols+'&types=chart&range='+window).json()
		elif window == 'dynamic':
			data = requests.get(base_url + symbols+'/chart/dynamic').json()
		else:
			data = requests.get(base_url + symbols+'/chart/date/'+window).json()
		if not data:
			print('Empty data set returned')
			sys.exit(1)
		else:
			return data

	def live_price(self, stock_name):
		json = self.get_batch(stock_name, 'dynamic')
		if json['range'] == 'today':
			print("Trading day has ended")
			return 0
		else:
			return int(json['data'][-1]['average'])


def main(required_option='1y', other_option=None):
		batch = StockBatch()
		batch.download(required_option, other_option)


if __name__ == '__main__':
	time_options = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m', '1d']
	try:
		if len(sys.argv) == 1:
			main()
			sys.exit(1)
			
		elif len(sys.argv) == 2 and sys.argv[1] in time_options:
			main(sys.argv[1])
			sys.exit(1)
			
		elif len(sys.argv) == 3 and len(sys.argv[2]) == 8:
			if isinstance(int(sys.argv[2]), int):
				main(sys.argv[1], sys.argv[2])
				sys.exit(1)
				
		elif len(sys.argv) == 3 and sys.argv[2] == 'dynamic':
			main(sys.argv[1], 'dynamic')
			sys.exit(1)
			
		else:
			print("--invalid requests--\nUSAGE= StockData.py [TIME_WINDOW]\n" +
				"| [STOCK_NAME NUMERICAL_DATE] | [STOCK_NAME dynamic]\n" +
				"Default command is batch request of 1 year\n" +
				"This program can return 3 types of requests:\n" +
				"\tSaves a large batch requests with an optional time window of 1 day to 5 years to file.\n" +
				"\tPrints a specific date's minute day for one stock." +
				" This is only applicable for the last 30 days. \n" +
				"\tDynamic will print today's minute data if called on during market hours.")
				
	except ValueError:
		print("Date request format bad.\nExample: 20190502 for May 2nd, 2019")
