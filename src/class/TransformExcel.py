import pandas as pd

class TransformExcel:
    def __init__(self, name_file, sheet='sb'):
        self.name_file = name_file
        try:
            self.df = pd.read_excel(f'../files/raw/{name_file}', sheet_name=sheet)
        except:
            raise(f'Erro: zip; file {self.name_file}')
        self.run()
    

    def getDate(self):
        self.df['date'] = self.df.iloc[1,5].strftime("%m/%d/%Y")
    
    def getGP(self):
        self.df['gp'] = self.df.iloc[0,7]


    def fillLastLocal(self):
        self.df.reset_index(inplace=True)
        self.df.drop(['index'], axis=1, inplace=True)

        for i in range(1,len(self.df)):
            if pd.isna(self.df.loc[i, 'pb']):
                self.df.loc[i, 'pb'] = self.df.loc[i-1, 'pb']

            if pd.isna(self.df.loc[i, 'eq']):
                self.df.loc[i, 'eq'] = self.df.loc[i-1, 'eq']

            if pd.isna(self.df.loc[i, 'road']):
                self.df.loc[i, 'road'] = self.df.loc[i-1, 'road']

    def formatColumns(self):
        cols = list(self.df.columns)
        date_position = cols.index('date')
        gp_position = cols.index('gp')
        self.df = self.df.loc[self.df.iloc[:,9]==1,:].iloc[:,[0,1,2,3,4,5,7,9, date_position, gp_position]]
        self.df.columns = ['road','roadByworker','begin','end','pb','eq','worker','rowTrue', 'date', 'gp']
        self.df = self.df[['gp', 'date', 'road','roadByworker','begin','end','pb','eq','worker','rowTrue']]
    
    def transform_to_str(self):
        for c in self.df.columns:
            self.df[c] = self.df[c].apply(lambda x: str(x).strip().lower() if x!=None else None)
            self.df[c] = self.df[c].apply(lambda x: ' '.join(x.split('-')) if x!=None else None)
            self.df[c] = self.df[c].apply(lambda x: '_'.join(x.split(' ')) if x!=None else None)
    
    def mapAreasbyRoad(self):
        self.df['areas'] = self.df[self.df['road'].str.len()>=3]['road'].apply(lambda x: x[0] if x[0] in ['1','2','3','4','5','6'] else x[:3])
        self.df.loc[self.df['pb'].isin(['selve_supervisão','sevop', 'selve_retiro','selve_dom avelar','selve_orlando_gomes' , 'serat','sefit']),'areas'] = 'interno'

        self.df.loc[self.df['road'].str.len()<3,'areas'] = 'inteligencia'
    
    @staticmethod
    def getInternWorkers(df):
        inHouse = df.loc[df['areas'] == 'interno',:]
        return list(inHouse.index)
    
    @staticmethod
    def getNoa(df):
        noa = df.loc[df['areas'] == 'inteligencia',:]
        noa = noa[noa['pb'].str.contains('n.o.a')]
        return list(noa.index)


    @staticmethod
    def save(df, nameCSV):
        df.to_csv(f'../files/db_format/{nameCSV}.csv', index=False)
    
    def run(self):
        self.getDate()
        self.getGP()
        self.formatColumns()
        self.fillLastLocal()
        self.transform_to_str()
        self.mapAreasbyRoad()
    
    def getDF(self):
        return self.df

if __name__ == '__main__':

    import os

    excelFiles = list(os.listdir('../files/raw/'))
    for fds in ['sb']:
        df = TransformExcel(excelFiles[0], sheet=fds).getDF()
        for xlsx in excelFiles[1:]:
            try:
                print(f'RUN: {xlsx}')
                df = pd.concat([df,TransformExcel(xlsx, sheet=fds).getDF()])
                print(f'OK: {xlsx}')
            except ValueError:
                print(f'ERROR: {xlsx}')
        
        TransformExcel.save(df, f'escala_full_{fds}')

        df = df.reset_index(drop=True)
        index_inHouse = set(TransformExcel.getInternWorkers(df))
        index_noa = set(TransformExcel.getNoa(df))
        index_op = set(df.index.to_list())-(index_inHouse.union(index_noa))

        op = df.loc[index_op,:].drop(['roadByworker'], axis=1)
        inH = df.loc[index_inHouse,:].drop(['road', 'roadByworker','eq', 'rowTrue', 'areas'], axis=1)
        noa = df.loc[index_noa,:].drop(['road', 'roadByworker', 'pb', 'rowTrue', 'areas'], axis=1)
        TransformExcel.save(op, f'escala_op_{fds}')
        TransformExcel.save(df.loc[index_inHouse,:], f'escala_inHouse_{fds}')
        TransformExcel.save(df.loc[index_noa,:], f'escala_noa_{fds}')
