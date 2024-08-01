class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        withoutSpace=key.replace(" ","")
        dict={" ":" "}
        f=97
        
        
        for i in withoutSpace:
            if i not in dict:
                dict[i]=chr(f)
                f=f + 1

        result=""
        for i in message:
            result+=dict[i]

        return result


        