from torch_rbf import *

class FancyKernel:

  def __init__(self,sigma_w,hidden_dim):
    self.K_theta=
    self.sigma_w=sigma_w
    self.M=
    self.optimizer= optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
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
    sum=0 #CONVERT TO PYTORCH TENSOR?
    for i in range(x.size()[0]):
      sum+=self.calc_likelihood(x[i,:],y[i,:])
    return sum
  def train(self,data):
    for i in range(10):
      loss=self.forward(data)
      print(loss.data)
      loss.backward()
      optimizer.step()
 
     
     
    
