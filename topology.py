#!/usr/bin/python

from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo

class fatTreeTopo(Topo):

    "Fat Tree Topology"

    def __init__(self):
        "Create Fat tree Topology"

        Topo.__init__(self)

        #Add hosts
		h1 = self.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
        h4 = self.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
        h3 = self.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
        h5 = self.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
        h6 = self.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
		h7 = self.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
        h8 = self.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
		h9 = self.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
		h10 = self.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
		h11 = self.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
		h12 = self.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)

        #Add switches
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch)
		s2 = self.addSwitch('s2', cls=OVSKernelSwitch)
		s3 = self.addSwitch('s3', cls=OVSKernelSwitch)
		s4 = self.addSwitch('s4', cls=OVSKernelSwitch)
		s5 = self.addSwitch('s5', cls=OVSKernelSwitch)
		s6 = self.addSwitch('s6', cls=OVSKernelSwitch)
		s7 = self.addSwitch('s7', cls=OVSKernelSwitch)
		s8 = self.addSwitch('s8', cls=OVSKernelSwitch)
		s9 = self.addSwitch('s9', cls=OVSKernelSwitch)
		s10 = self.addSwitch('s10', cls=OVSKernelSwitch)
		s11 = self.addSwitch('s11', cls=OVSKernelSwitch)
		s12 = self.addSwitch('s12', cls=OVSKernelSwitch)
		s13 = self.addSwitch('s13', cls=OVSKernelSwitch)
		s14 = self.addSwitch('s14', cls=OVSKernelSwitch)
		s15 = self.addSwitch('s15', cls=OVSKernelSwitch)

        #Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(h7, s4)
        self.addLink(h8, s4)
		self.addLink(h9, s5)
		self.addLink(h10, s5)
		self.addLink(h11, s6)
		self.addLink(h12, s6)
		self.addLink(s1, s7)
		self.addLink(s1, s8)
		self.addLink(s2, s7)
		self.addLink(s2, s8)
		self.addLink(s3, s9)
		self.addLink(s3, s10)
		self.addLink(s4, s9)
		self.addLink(s4, s10)
		self.addLink(s5, s11)
		self.addLink(s5, s12)
		self.addLink(s6, s11)
		self.addLink(s6, s12)
		self.addLink(s7, s13)
		self.addLink(s8, s15)
		self.addLink(s9, s13)
		self.addLink(s10, s14)
		self.addLink(s11, s14)
		self.addLink(s12, s15)

topos = { 'mytopo': (lambda: fatTreeTopo() ) }