from bitcoin.rpc import RawProxy
import hashlib
import codecs
import struct


def Compare():
    p = RawProxy()
    blockHash = p.getblockhash(input("block height:"))
    block = p.getblock(blockHash)
    hex = (Endian(block['version']) + ReOrder(block['previousblockhash']) + ReOrder(block['merkleroot']) + Endian(
        block['time']) + ReOrder(block['bits']) + Endian(block['nonce']))
    FullHash = codecs.decode(
        codecs.encode(hashlib.sha256(hashlib.sha256(codecs.decode(hex, 'hex')).digest()).digest()[::-1], 'hex_codec'))
    print("Block Hash", blockHash)
    print("Verif Hash", FullHash)
    print("Same : ", blockHash == FullHash)

def Endian(Numb):
    return codecs.encode(struct.pack("<I", Numb), 'hex').decode()


def ReOrder(Line):
    Swapper = list(Line[::-1])
    Swapped = ""
    for i in range(0, len(Swapper), 2):
        Swapped = Swapped + (Swapper[i + 1] + Swapper[i])
    return Swapped


Compare()
