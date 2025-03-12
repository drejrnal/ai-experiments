import torch;

x1 = torch.tensor([2.0]).double();
x1.requires_grad = True;

print(x1);
print(x1.data.item());