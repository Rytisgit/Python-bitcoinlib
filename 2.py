from bitcoin.rpc import RawProxy
import hashlib
import codecs
import struct


def Compare():
    p = RawProxy()
    blockHash = p.getblockhash(input("block height:"))
    block = p.getblock(blockHash)
    hex = (CalcEndian(block['version']) + ReOrder(block['previousblockhash']) + ReOrder(block['merkleroot']) + CalcEndian(
        block['time']) + ReOrder(block['bits']) + CalcEndian(block['nonce']))
    FullHash = codecs.decode(
        codecs.encode(hashlib.sha256(hashlib.sha256(codecs.decode(hex, 'hex')).digest()).digest()[::-1], 'hex_codec'))
    print("Block Hash", blockHash)
    print("Verif Hash", FullHash)
    print("Same : ", blockHash == FullHash)

def CalcEndian(number):
    return codecs.encode(struct.pack("<I", number), 'hex').decode()

def ReOrder(line):
    List = list(line[::-1])
    swap = ""
    for i in range(0, len(List), 2):
        swap = swap + (List[i + 1] + List[i])
    return swap


Compare()
