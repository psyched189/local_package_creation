!pip install -e . 
from test_package import Configuration, stack, linked_list

ll = linked_list.LinkedList()
st = stack.Stack()
config = Configuration()

for i in range(1,11):
	ll.append(i)

ll.head.print_nodes()

for i in range(11,21):
	st.push(i)

st.print_stack()
st.pop()
st.print_stack()

config.add(10,0)
config.add(20,1)

config.print_config()
