func helper(board [][]byte, word string, k int, row int, col int,n int ,m int) bool {
    if k == len(word) {
        return true
    }
    if k > len(word) {
        return false
    }

    dirs := [][] int {{0,1},{1,0},{-1,0},{0,-1}}
    res :=false
    for _,dir := range(dirs) {
        r:=row+dir[0]
        c:=col+dir[1]
        
        if r<n && c< m && r>=0 && c>=0 && board[r][c]!='#' && board[r][c]==word[k] {
            val := board[r][c]
            board[r][c]='#'
            res=res || helper(board,word,k+1,r,c,n,m)
            board[r][c]=val
        }
    }
    return res
}

func exist(board [][]byte, word string) bool {
    n:=len(board)
    m:=len(board[0])

    for i:=0; i<n; i++ {
        for j:=0; j<m; j++ {
            
            if word[0]==board[i][j] {
                val :=board[i][j]
                board[i][j]='#'
                res:=helper(board,word,1,i,j,n,m)
                if res {
                    return res
                }
                board[i][j]=val
            }
        }
    }
    return false
}