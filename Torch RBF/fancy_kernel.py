from torch_rbf import *

class FancyKernel:

  def __init__(self,sigma_w,hidden_dim):
    self.K_theta=
    self.sigma_w=sigma_w
    self.M=
  def transform_inputs(x):
    ''''
    x.dim = (n,2)
    M.dim = (2,hidden_dim)
    ''''
    return torch.matmul(x,self.M).data.numpy
  def calc_likelihood(self,x,y):
    ##CALC LIKELIHOOD IN LOG PROB FORM##
    return -1 *likelihood #in log probability form
  def forward(self,data):
    '''
    data is [x,y]
    '''
    x=transform_inputs(data[0])
    y=data[1]
    return self.calc_likelihood(x,y)
  def train(self,data)
    loss=self.forward(data)
    loss.backward()
    ###put in some optimizer! stop when loss stops decreasing? or for 10 epochs?###
     
     
    
