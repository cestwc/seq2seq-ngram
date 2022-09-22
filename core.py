import torch
import torch.nn.functional as F

w11 = torch.tensor([[[[0., 0.],
                      [0., 1.]]],
                    
                    [[[0., 0.],
                      [1., 1.]]],
                    
                    [[[0., 1.],
                      [0., 1.]]]]
                  )

w12 = torch.tensor([[[[0., 0.],
                      [0., 1.]],
                     
                     [[0., 0],
                      [0,  0]],
                     
                     [[0., 0],
                      [0,  0]]],
                    
                    [[[0., 0],
                      [0,  1]],
                     
                     [[0., 0],
                      [1,  0]],
                     
                     [[0., 0],
                      [0,  0]]],
                    
                    [[[0., 0],
                      [0,  1]],
                     
                     [[0., 0],
                      [0,  0]],
                     
                     [[0., 1],
                      [0,  0]]]]
                  )

def sudoku(x):
	
	x = F.conv2d(F.pad(x, (1, 0, 1, 0)), w1)
	for i in range(100):
		x = F.conv2d(F.pad(x, (1, 0, 1, 0)), w2)

	return F.relu(F.relu(1 - abs(x[:, 1:2] - x[:, 2:3]))  + x[:, 0:1] - 1)

def diagonal2(x):
	x = F.conv2d(F.pad(x, (1, 0, 1, 0)),
				 torch.tensor([[[[1., 0],
								 [0, 1]]]]
							 )
				)
	return F.relu(x - 1)


