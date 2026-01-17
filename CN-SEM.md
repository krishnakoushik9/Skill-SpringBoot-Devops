### Introduction
- [x] Network  
- [x] Data Communication  
- [x] Components of Data Communication  
  - [x] Message  
  - [x] Sender  
  - [x] Receiver  
  - [x] Transmission Medium  
  - [x] Protocol  
- [x] Distributed Processing  
- [x] Network Criteria  
  - [x] Performance  
  - [x] Reliability  
  - [x] Security  
- [x] Physical Structures  
  - [x] Type of Connection  
    - [x] Point-to-Point  
    - [x] Multipoint  
  - [x] Physical Topology  
    - [x] Mesh  
    - [x] Star  
    - [x] Bus  
    - [x] Ring  

### Uses of Computer Networks
- [x] Business Applications  
  - [x] Resource Sharing  
  - [x] Server–Client Model  
  - [x] Communication Medium  
  - [x] E-Commerce  
- [x] Home Applications  
  - [x] Access to Remote Information  
  - [x] Person-to-Person Communication  
  - [x] Interactive Entertainment  
  - [x] Electronic Commerce  

### Types / Categories of Networks
- [ ] LAN (Local Area Network)  
- [ ] MAN (Metropolitan Area Network)  
- [ ] WAN (Wide Area Network)  

### The Internet
- [ ] Brief History  
- [ ] ARPANET  
- [ ] NCP → TCP  
- [ ] Transition to TCP/IP  
- [ ] The Internet Today  
  - [ ] International ISPs  
  - [ ] National ISPs  
  - [ ] Regional ISPs  
  - [ ] Local ISPs  

### Reference Models
- [x] TCP/IP Model  
- [x] OSI Model  
- [x] Comparison of OSI and TCP/IP Models  

### Network Architecture
- [x] Peer-to-Peer Network  
- [x] Client/Server Network  

### Physical Layer

#### Guided Transmission Media
- [x] Twisted-Pair Cable  
- [x] Coaxial Cable  
- [x] Fiber-Optic Cable  

#### Unguided (Wireless) Transmission Media
- [x] Radio Waves  
- [x] Microwaves  
- [x] Infrared  
### Data Link Layer

- [x] Introduction to Data Link Layer  
- [x] Responsibilities of DLL  
  - [x] Framing  
  - [x] Addressing  
  - [x] Flow Control  
  - [x] Error Control  
  - [x] Media Access Control  

### Data Link Layer Design Issues
- [ ] Services Provided to the Network Layer  
- [ ] Framing  
- [ ] Error Control  
- [ ] Flow Control  

### Error Detection & Correction
- [x] Types of Errors  
  - [x] Single Bit Error  
  - [x] Multiple Bit Error  
  - [x] Burst Error  
- [x] Error Detection  
  - [x] Parity Check  
  - [x] Cyclic Redundancy Check (CRC)  
- [ ] Error Correction  
  - [ ] Backward Error Correction  
  - [ ] Forward Error Correction  

### Elementary Data Link Protocols
- [x] Simplex Protocol  
- [x] Stop-and-Wait Protocol  
- [ ] Stop-and-Wait ARQ  
- [x] Go-Back-N ARQ  
- [x] Selective Repeat ARQ  

### Sliding Window Protocols
- [ ] Sending Window  
- [ ] Receiving Window  
- [ ] Sequence Numbers  
- [x] Go-Back-N ARQ  
- [x] Selective Repeat ARQ  

### Multiple Access Protocols

#### Random Access Protocols
- [x] ALOHA  
  - [x] Pure ALOHA  
  - [x] Slotted ALOHA  
- [x] CSMA  
  - [x] 1-Persistent  
  - [x] Non-Persistent  
  - [x] p-Persistent  
  - [x] 0-Persistent  
- [x] CSMA/CD  
  - [x] Collision Detection  
  - [x] Back-off Algorithm  
- [x] CSMA/CA  
  - [x] Inter Frame Space (IFS)  
  - [x] Contention Window  
  - [x] Acknowledgment  
#### Controlled Access Protocols
- [ ] Reservation  
- [ ] Polling  
- [ ] Token Passing  
### Collision-Free Protocols
- [ ] Bit-map Protocol  
- [ ] Binary Countdown  
- [ ] Limited Contention Protocols  
- [ ] Adaptive Tree Walk Protocol  

### Medium Access Sublayer (MAC)
- [ ] Concepts of MAC  
- [ ] Who gets to use the channel?  

### Data Link Layer Switching
- [x] Switching Bridges  
  - [x] Transparent Basic Bridge  
  - [x] Source Routing Bridge  
  - [x] Transparent Learning Bridge  
  - [x] Transparent Spanning Tree Bridge  
- [x] Spanning Tree Protocol (STP)  

### Network Devices
- [x] Repeater  
- [x] Hub  
- [x] Switch  
- [x] Router  
- [x] Gateway  
- [x] B-router  
-----
## UNIT - IV

### Introduction to Transport Layer
- [x] Responsibilities of Transport Layer  
  - [x] Process-to-Process Delivery  
  - [x] Addressing (Port Numbers)  
  - [x] Encapsulation & Decapsulation  
  - [x] Multiplexing  
  - [x] Demultiplexing  
  - [x] Flow Control  
  - [x] Error Control  
  - [x] Congestion Control  

### Transport Layer Protocols
- [x] TCP (Transmission Control Protocol)  
  - [x] Features of TCP  
    - [x] Connection-Oriented  
    - [x] Reliable  
    - [x] Full Duplex  
    - [x] Stream Delivery  
    - [x] Error Control  
    - [x] Flow Control  
    - [x] Congestion Control  
  - [x] TCP Services  
  - [x] TCP Segment Format  
  - [x] TCP Connection Establishment (Three-Way Handshake)  
  - [x] TCP Connection Termination (Four-Way Handshake)  
  - [x] Flow Control using Sliding Window  
  - [x] Error Control (Checksum, Retransmission)  
  - [x] Congestion Control  
    - [x] Slow Start  
    - [x] Congestion Avoidance  
    - [x] Fast Retransmit  
    - [x] Fast Recovery  

- [x] UDP (User Datagram Protocol)  
  - [x] Features of UDP  
    - [x] Connectionless  
    - [x] Unreliable  
    - [x] Fast  
    - [x] Low Overhead  
  - [x] UDP Segment Format  
  - [x] Use Cases of UDP  

### Congestion Control Mechanisms
- [x] Congestion Causes  
- [x] Congestion Prevention Policies  
  - [x] Open Loop Congestion Control  
  - [x] Closed Loop Congestion Control  
- [x] Congestion Control Techniques  
  - [x] Slow Start  
  - [x] Additive Increase Multiplicative Decrease (AIMD)  
  - [x] Fast Retransmit  
  - [x] Fast Recovery  

### QoS (Quality of Service)
- [x] QoS Definition  
- [x] Flow Characteristics  
  - [x] Reliability  
  - [x] Delay  
  - [x] Jitter  
  - [x] Bandwidth  
- [x] Techniques to Improve QoS  
  - [x] Scheduling  
  - [x] Traffic Shaping (Leaky Bucket / Token Bucket)  
  - [x] Resource Reservation  
  - [x] Admission Control  

### Transport Layer Addressing
- [x] Port Numbers  
  - [x] Well-Known Ports  
  - [x] Registered Ports  
  - [x] Dynamic Ports  

### Connection Establishment Issues
- [x] Three-Way Handshake Problems  
- [x] Half Open Connections  
- [x] SYN Flooding Attack

----
## UNIT - V

### Domain Name System (DNS)
- [x] Introduction to DNS  
- [x] Need for DNS  
- [x] How DNS Works  
- [x] DNS Hierarchical Structure  
  - [x] Root DNS Server  
  - [x] Top-Level Domain Servers  
  - [x] Authoritative Servers  
- [x] Types of DNS Domains  
  - [x] Generic Domains (.com, .org, .edu ...)  
  - [x] Country Domains (.in, .uk, .au ...)  
  - [x] Inverse Domains  
- [x] DNS Query Types  
  - [x] Recursive Query  
  - [x] Iterative Query  
- [x] Resolver  
- [x] Name Servers  

### Simple Network Management Protocol (SNMP)
- [x] SNMP Definition  
- [x] SNMP Components  
  - [x] SNMP Manager  
  - [x] SNMP Agent  
  - [x] Management Information Base (MIB)  
- [x] SNMP Messages  
  - [x] GetRequest  
  - [x] GetNextRequest  
  - [x] GetBulkRequest  
  - [x] SetRequest  
  - [x] Response  
  - [x] Trap  
  - [x] InformRequest  
- [x] SNMP Security Levels  
  - [x] noAuthNoPriv  
  - [x] authNoPriv  
  - [x] authPriv  
- [x] SNMP Versions  
  - [x] SNMPv1  
  - [x] SNMPv2  
  - [x] SNMPv3  

### Electronic Mail (E-Mail)
- [x] Introduction & History  
- [ ] Components of Email System  
  - [x] User Agent (UA)  
  - [x] Message Transfer Agent (MTA)  
  - [x] Mailbox  
  - [x] Spool File  
- [x] Email Services  
  - [x] Composition  
  - [x] Transfer  
  - [x] Reporting  
  - [x] Displaying  
  - [x] Disposition  
- [x] Email Format  
  - [x] Envelope  
  - [x] Header  
    - [x] To  
    - [x] CC  
    - [x] BCC  
    - [x] From  
    - [x] Sender  
    - [x] Received  
    - [x] Return-Path  
  - [x] Body  

### IMAP vs POP3
- [x] Meaning  
- [x] Port Numbers  
- [x] Accessibility  
- [x] Readability  
- [x] Mail Organization  
- [x] Updating  
- [x] Storage Differences  

### World Wide Web (WWW)
- [ ] Introduction to WWW  
- [ ] History  
- [ ] Components of the Web  
  - [ ] URL  
  - [ ] HTTP  
  - [ ] HTML  
  - [ ] XML  
- [ ] Architecture of WWW  
  - [ ] Client/Browser  
  - [ ] Server  
- [ ] Features of WWW  
- [ ] Advantages & Disadvantages  

### HyperText Transfer Protocol (HTTP)
- [ ] Features  
  - [ ] Connectionless  
  - [ ] Stateless  
  - [ ] Media Independent  
- [ ] HTTP Messages  
  - [ ] Request Message  
  - [ ] Response Message  
- [ ] HTTP Operations (GET, POST, etc.)  

### Streaming Audio/Video
- [x] Introduction to Streaming  
- [x] Categories  
  - [x] Streaming Stored Audio/Video  
  - [x] Streaming Live Audio/Video  
  - [x] Real-Time Interactive Audio/Video  
- [ ] Approaches for Stored Streaming  
  - [ ] Web Server Only  
  - [ ] Web Server + Metafile  
  - [ ] Media Server  
  - [ ] Media Server + RTSP  
- [x] Concepts  
  - [x] Jitter  
  - [x] Timestamp  
  - [x] UDP vs TCP in Streaming  
---
Notes : ![[COMPUTER NETWORKS-R22.pdf]]
![[CN UNIT-1 BY BK_CHINNA.pdf]]
![[CN UNIT-2 BY BK_CHINNA.pdf]]

![[CN UNIT-4 BY BK_CHINNA.pdf]]

![[CN UNIT-5 BY BK_CHINNA.pdf]]