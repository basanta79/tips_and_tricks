/** This tip is for encapsulate the call to an array in a function
 *  and when you want to call this function you can see options you have
 *  you can also increase functionality because you are accessing the 
 *  the const dictionary using a function. 
 */

const MESSAGES = {
    hello: 'hello',
    bye: 'goodbye'
}

type MessageKey = keyof typeof MESSAGES

function reply(msg: MessageKey){
    return MESSAGES['msg']
}


/* When you want to call reply function when you type ' to write
   the argument you will see as intelisense the options you have */

reply('')