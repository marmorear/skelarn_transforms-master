  
de  sklearn . importação de base  BaseEstimator , TransformerMixin 
importar  imblearn
de  imblearn . over_sampling  import  SMOTE
importar  pandas  como  pd
from sklearn.ensemble import GradientBoostingClassifier

dtc_model = GradientBoostingClassifier() 


# Todas as transformações sklearn devem ter os métodos `transform` e` fit`
classe  DropColumns ( BaseEstimator , TransformerMixin ):
    def  __init__ ( self , colunas ):
        eu . colunas  =  colunas

    def  fit ( self , X , y = None ):
        retornar a  si mesmo

    def  transform ( self , X ):
        # Primeiro realiza uma cópia do dataframe 'X' de entrada
        Dados  =  X . cópia ()
        # Retornamos um novo dataframe sem as colunas indesejadas
         dados de retorno . descartar ( rótulos = auto . colunas , eixo = 'colunas' )
    
classe  SetIndex ( BaseEstimator , TransformerMixin ):
    def  __init__ ( self , colunas ):
        eu . colunas  =  colunas

    def  fit ( self , X , y = None ):
        retornar a  si mesmo

    def  transform ( self , X ):
        # Primeiro realiza uma cópia do dataframe 'X' de entrada
        Dados  =  X . cópia ()
        # Retornamos um novo dataframe sem as colunas indesejadas
         dados de retorno . set_index ( auto . colunas , inplace = Verdadeiro )
    
   
classe  SmoteResample ( objeto ):
    def  __init__ ( self ):
        passar

    def  fit ( self , X , y ):
        X_resampled , y_resampled  =  SMOTE (). fit_resample ( X , y )
        X_resampled  =  pd . Trama de dados ( X_resampled , colunas = X . Colunas )
        return  X_resampled , y_resampled



