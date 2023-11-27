using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Chess
{
    public class ChessBoard
    {
        private ChessPiece[,] boardArray;
        private const int COLUMNS = 8;
        private const int ROWS = 8;
        public int Turn { get; set; }
        public int Mat { get; set; }

        public ChessBoard()
        {
            Mat = 0;
            Turn = 1;
            SetupBoard();
        }

        public int GetLength(int l)
        {
            return boardArray.GetLength(l);
        }

        public ChessPiece this[int x, int y]
        {
            get { return boardArray[x, y]; }
        }

        private ChessBoard SetupBoard()
        {
            boardArray = new ChessPiece[COLUMNS, ROWS];
            string[] playerPeices = {
                "Rook", "Knight", "Bishop", "Queen",
                "King", "Bishop", "Knight", "Rook",
                "Pawn", "Pawn", "Pawn", "Pawn",
                "Pawn", "Pawn", "Pawn", "Pawn" };

            for (int i = 0; i < COLUMNS; i++)
            {
                // Player 0 pieces
                boardArray[i, 0] =          (ChessPiece)Activator.CreateInstance(
                                                Type.GetType("Chess." + playerPeices[i]));
                boardArray[i, 1] =          (ChessPiece)Activator.CreateInstance(
                                                Type.GetType("Chess." + playerPeices[i + COLUMNS]));
                // Player 1 pieces
                boardArray[i, ROWS - 1] =   (ChessPiece)Activator.CreateInstance(
                                                Type.GetType("Chess." + playerPeices[i]), new object[] { 1 });
                boardArray[i, ROWS - 2] =   (ChessPiece)Activator.CreateInstance(
                                                Type.GetType("Chess." + playerPeices[i + COLUMNS]), new object[] { 1 });
            }
            return this;
        }

       
        public IEnumerable<Point> PosiblePieceActions(int x, int y, bool ignoreCheck = false, bool attackActions = true, bool moveActions = true, ChessPiece[,] boardArray = null)
        {
            if (boardArray == null)
            {
                boardArray = this.boardArray;
            }

            bool[,] legalActions = new bool[boardArray.GetLength(0), boardArray.GetLength(1)];
            List<Point> availableActions = new List<Point>();
            ChessPiece movingPeice = boardArray[x, y];
            
            if (attackActions)
            {
                foreach (Point[] direction in movingPeice.AvailableAttacks)
                {
                    foreach (Point attackPoint in direction)
                    {
                        Point adjustedPoint = new Point(attackPoint.x + x, attackPoint.y + y);
                        if (ValidatePoint(adjustedPoint))
                        {
                            if (boardArray[adjustedPoint.x, adjustedPoint.y] != null
                                && boardArray[adjustedPoint.x, adjustedPoint.y].Player ==
                                movingPeice.Player) break;
                            if (boardArray[adjustedPoint.x, adjustedPoint.y] != null)
                            {
                                AddMove(availableActions, new Point(x, y), adjustedPoint, ignoreCheck);
                                break;
                            }
                        }
                    }
                }
            }

            if (moveActions)
            {
                foreach (Point[] direction in movingPeice.AvailableMoves)
                {
                    foreach (Point movePoint in direction)
                    {
                        Point adjustedPoint = new Point(movePoint.x + x, movePoint.y + y);
                        if (ValidatePoint(adjustedPoint))
                        {
                            if (boardArray[adjustedPoint.x, adjustedPoint.y] != null) break;
                            AddMove(availableActions, new Point(x, y), adjustedPoint, ignoreCheck);
                        }
                    }
                }
            }

            if (movingPeice is King && ((King)movingPeice).CanCastle)
            {
                int rookX = 0;
                if (boardArray[rookX, y] is Rook && ((Rook)boardArray[rookX, y]).CanCastle)
                {
                    bool missedCondition = false;
                    foreach (int rangeX in Enumerable.Range(rookX + 1, Math.Abs(rookX - x) - 1))
                    {
                        if (boardArray[rangeX, y] != null) missedCondition = true;
                       
                    }
                    
                    missedCondition = missedCondition || KingInCheck(movingPeice.Player);
                    if (!missedCondition) 
                        AddMove(availableActions, new Point(x, y), new Point(x - 2, y), ignoreCheck);
                }
                rookX = COLUMNS - 1;
                if (boardArray[rookX, y] is Rook && ((Rook)boardArray[rookX, y]).CanCastle)
                {
                    bool missedCondition = false;
                    foreach (int rangeX in Enumerable.Range(x + 1, Math.Abs(rookX - x) - 1))
                    {
                        if (boardArray[rangeX, y] != null) missedCondition = true;
                       
                    }
                    
                    missedCondition = missedCondition || KingInCheck(movingPeice.Player);
                    if (!missedCondition) 
                        AddMove(availableActions, new Point(x, y), new Point(x + 2, y), ignoreCheck);
                }
            }

            if (movingPeice is Pawn)
            {
                Pawn pawn = (Pawn)movingPeice;
                int flipDirection = 1;

                if (pawn.Player == 1) flipDirection = -1;
                if (pawn.CanEnPassantLeft)
                {
                    Point attackPoint;
                    attackPoint = ChessPiece.GetDiagnalMovementArray(1, DiagnalDirection.FORWARD_LEFT)[0];
                    attackPoint.y *= flipDirection;
                    attackPoint.y += y;
                    attackPoint.x += x;
                    if (ValidatePoint(attackPoint))
                    {
                        AddMove(availableActions, new Point(x,y), attackPoint, ignoreCheck);
                    }
                }

                if (pawn.CanEnPassantRight)
                {
                    Point attackPoint;
                    attackPoint = ChessPiece.GetDiagnalMovementArray(1, DiagnalDirection.FORWARD_RIGHT)[0];
                    attackPoint.y *= flipDirection;
                    attackPoint.y += y;
                    attackPoint.x += x;
                    if (ValidatePoint(attackPoint))
                    {
                        AddMove(availableActions, new Point(x, y), attackPoint, ignoreCheck);
                    }
                }
            }
            
            return availableActions;
        }

        private void AddMove(List<Point> availableActions, Point fromPoint, Point toPoint, bool ignoreCheck = false)
        {
            bool kingInCheck = false;

            if (!ignoreCheck)
            {
                ChessPiece movingPiece = boardArray[fromPoint.x, fromPoint.y];
                ChessPiece[,] boardArrayBackup = (ChessPiece[,])boardArray.Clone();
                MakePieceAction(fromPoint, toPoint, true);
                kingInCheck = KingInCheck(movingPiece.Player);
                boardArray = boardArrayBackup;
            }

            if (ignoreCheck || !kingInCheck) availableActions.Add(toPoint);
        }
        private bool Isdraw()
        {

            int BishopcountB = 0;
            int KnitecountB = 0;
            int BishopcountW = 0;
            int KnitecountW = 0;
            for (int x = 0; x < COLUMNS; x++)
            {
                for (int y = 0; y < ROWS; y++)
                {
                    ChessPiece chessPiece = boardArray[x, y];
                    if (chessPiece is Rook || chessPiece is Queen || chessPiece is Pawn) { return false; }
                    if (chessPiece is Bishop)
                        if (chessPiece.Player == 1)
                            BishopcountB++;
                        else
                            BishopcountW++;
                    if (chessPiece is Knight)
                        if (chessPiece.Player == 1)
                            KnitecountB++;
                        else
                            KnitecountW++;
                }

            }
            if (KnitecountB + BishopcountB >= 2 || KnitecountW + BishopcountW >= 2) return false;
            return true;
        }
        public bool KingInCheck(int player)
        {
            for (int x = 0; x < COLUMNS; x++)
            {
                for (int y = 0; y < ROWS; y++)
                {
                    ChessPiece chessPiece = boardArray[x, y];
                    if (chessPiece != null
                        && chessPiece.Player == player
                        && chessPiece is King)
                    {
                        if (CheckSquareVulnerable(x, y, player))
                        {
                           
            
                            return true;
                        }
                        else
                        {
                            return false;
                        }
                    }
                }
            }
            return false;
        }

        public IEnumerable<Point> PosiblePieceActions(Point position, bool ignoreCheck = false, bool attackActions = true, bool moveActions = true, ChessPiece[,] boardArray = null)
        {
            return PosiblePieceActions(position.x, position.y, ignoreCheck, attackActions, moveActions, boardArray);
        }
        public bool MakePieceAction(int fromX, int fromY, int toX, int toY)
        {
            
            return MakePieceAction(new Point(fromX, fromY), new Point(toX, toY));
        }



        public bool MakePieceAction(Point from, Point to, bool bypassValidaiton = false)
        {
            if (Isdraw()) { Mat = 2; MessageBox.Show("Draw insufficient material",""  , MessageBoxButtons.OK); Application.Restart(); }
            if (Mat == 1) { Mat = 2; string odp = Turn == 1 ? " wygral czarny" : " wygral bialy"; MessageBox.Show("MAT " + odp, "", MessageBoxButtons.OK); Application.Restart(); }
            
            if (bypassValidaiton || (PosiblePieceActions(from).Contains(to) && boardArray[from.x,from.y].Player==Turn))
            {
                ChessPiece movingPeice = boardArray[from.x, from.y];
                if (movingPeice is Pawn)
                {
                    Pawn pawn = (Pawn)movingPeice;
                    
                    if (Math.Abs(from.y - to.y) == 2)
                    {
                        int adjasentX = to.x - 1;
                        if (adjasentX > -1
                            && boardArray[adjasentX, to.y] != null
                            && boardArray[adjasentX, to.y].Player != movingPeice.Player
                            && boardArray[adjasentX, to.y] is Pawn)
                        {
                            if (!bypassValidaiton) 
                                ((Pawn)boardArray[adjasentX, to.y]).CanEnPassantRight = true;
                        }
                        adjasentX += 2;
                        if (adjasentX < COLUMNS
                            && boardArray[adjasentX, to.y] != null
                            && boardArray[adjasentX, to.y].Player != movingPeice.Player
                            && boardArray[adjasentX, to.y] is Pawn)
                        {
                            if (!bypassValidaiton) 
                                ((Pawn)boardArray[adjasentX, to.y]).CanEnPassantLeft = true;
                        }
                    }
                    
                    if (from.x != to.x && boardArray[to.x, to.y] == null)
                    {
                        boardArray[to.x, from.y] = null;
                    }

                    if (!bypassValidaiton) 
                        pawn.CanDoubleJump = false; 
                }
                if (movingPeice is CastlePiece)
                {
                    CastlePiece rookOrKing = (CastlePiece)movingPeice;
                    if (!bypassValidaiton) 
                        rookOrKing.CanCastle = false; 
                }
                if (movingPeice is King)
                {
                    
                    King king = (King)movingPeice;
                    if (from.x - to.x == 2)
                    {  
                        boardArray[to.x + 1, from.y] = boardArray[0, from.y];
                        boardArray[0, from.y] = null;
                    }
                    if (from.x - to.x == -2)
                    {   
                        boardArray[to.x - 1, from.y] = boardArray[COLUMNS - 1, from.y];
                        boardArray[COLUMNS - 1, from.y] = null;
                    }
                }
                movingPeice.CalculateMoves();
                boardArray[from.x, from.y] = null;
                boardArray[to.x, to.y] = movingPeice;

                if (bypassValidaiton != true)
                {
                    if (CanPromote(movingPeice, to.x, to.y))
                    {
                        OptionForm optionForm = new OptionForm();
                        DialogResult result = optionForm.ShowDialog();

                        if (result == DialogResult.OK)
                        {
                            string wybor = optionForm.SelectedOption; 
                            Promotion(Turn, to, wybor);
                        }
                         }

                    Turn = (Turn + 1) % 2;
                    
                    if (KingInCheck(Turn))
                        if (IsCheckmate(Turn)) Mat = 1;
                       
                    
                }
                return true;
            }
            
            return false;
        }
        public void Promotion(int Turn,Point to,string Option)
        {
            if (Turn == 0)
            {
                boardArray[to.x, to.y] = (ChessPiece)Activator.CreateInstance(
                                    Type.GetType("Chess." + Option));
            }
            else
            {
                boardArray[to.x, to.y] = (ChessPiece)Activator.CreateInstance(
                                    Type.GetType("Chess." + Option), new object[] { 1 }); ;
            }
        }
        public bool CanPromote(ChessPiece movingPeice,int x,int y)
        {
            if (movingPeice is Pawn)
                if (y==0 || y==7)
                {
                    return true;
                }
            return false;

        }
        
        public bool CheckSquareVulnerable(int squareX, int squareY, int player, ChessPiece[,] boardArray = null)
        {
            if (boardArray == null)
            {
                boardArray = this.boardArray;
            }

            for (int x = 0; x < boardArray.GetLength(0); x++)
            {
                for (int y = 0; y < boardArray.GetLength(1); y++)
                {
                    if (boardArray[x, y] != null && boardArray[x, y].Player != player)
                    {
                        foreach (Point point in PosiblePieceActions(x, y, true, true, false, boardArray))
                        {
                            if (point.x == squareX && point.y == squareY)
                            {
                                return true;
                            }
                        }
                    }
                }
            }
            return false;
        }

        private bool IsCheckmate(int player)
        {
            
            for (int x = 0; x < COLUMNS; x++)
            {
                for (int y = 0; y < ROWS; y++)
                {
                    ChessPiece chessPiece = boardArray[x, y];
                    if (chessPiece != null && chessPiece.Player == player)
                    {
                        
                        IEnumerable<Point> actions = PosiblePieceActions(x, y);
                        foreach (Point action in actions)
                        {
                            ChessPiece[,] boardArrayCopy = (ChessPiece[,])boardArray.Clone();
                            if (MakePieceAction(new Point(x, y), action, true))
                            {
                                
                                if (!KingInCheck(player))
                                {
                                    boardArray = boardArrayCopy; 
                                    return false; 
                                }
                                boardArray = boardArrayCopy;
                            }
                        }
                    }
                }
            }
            return true; 
        }
        private bool ValidateRange(int value, int high, int low = -1)
        {
            return value > low && value < high;
        }

        public bool ValidateX(int value)
        {
            return ValidateRange(value, boardArray.GetLength(0));
        }

        public bool ValidateY(int value)
        {
            return ValidateRange(value, boardArray.GetLength(1));
        }

        public bool ValidatePoint(Point point)
        {
            return ValidateX(point.x) && ValidateY(point.y);
        }
    }
}
