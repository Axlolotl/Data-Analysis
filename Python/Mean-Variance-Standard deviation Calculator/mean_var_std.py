import numpy as np

def calculate(list):
      try:
         a=np.array(list)
         b=a.reshape((3,3))
      except:
        raise ValueError("List must contain nine numbers.")
      mean=[b.mean(axis=0).tolist(),b.mean(axis=1).tolist(), b.mean()]
      varian=[b.var(axis=0).tolist(),b.var(axis=1).tolist(),b.var()]
      std=[b.std(axis=0).tolist(),b.std(axis=1).tolist(),b.std()]
      mx=[b.max(axis=0).tolist(),b.max(axis=1).tolist(),b.max()]
      mn=[b.min(axis=0).tolist(),b.min(axis=1).tolist(),b.min()]
      sm=[b.sum(axis=0).tolist(),b.sum(axis=1).tolist(),b.sum()]
      calculations= { "mean": mean,"variance": varian,"standard deviation": std,"max": mx,"min": mn,"sum": sm}
      return calculations