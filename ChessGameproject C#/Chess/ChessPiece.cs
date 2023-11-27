using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chess
{
    public abstract class ChessPiece
    {
        protected const int MAX_DISTANCE = 7;

        protected bool canEnPassantLeft;
        protected bool canEnPassantRight;
        protected bool canDoubleJump;

       
        protected bool canCastle; 
        protected Point[][] availableMoves; 
        protected Point[][] availableAttacks; 
        private int player;

        public Point[][] AvailableMoves
        {
            get { return availableMoves; }
        }

        public Point[][] AvailableAttacks
        {
            get { return availableAttacks; }
        }

        public int Player
        {
            get { return player; }
            set { player = value; }
        } 

        public abstract ChessPiece CalculateMoves();

        public static Point[] GetMovementArray(int distance, Direction direction)
        {
            Point[] movement = new Point[distance];
            int xPosition = 0;
            int yPosition = 0;

            for (int i = 0; i < distance; i++)
            {
                switch (direction)
                {
                    case Direction.FORWARD:
                        yPosition++;
                        break;
                    case Direction.BACKWARD:
                        yPosition--;
                        break;
                    case Direction.LEFT:
                        xPosition++;
                        break;
                    case Direction.RIGHT:
                        xPosition--;
                        break;
                    default:
                        break;
                }
                movement[i] = new Point(xPosition, yPosition);
            }
            return movement;
        }

        public static Point[] GetDiagnalMovementArray(int distance, DiagnalDirection direction)
        {
            Point[] attack = new Point[distance];
            int xPosition = 0;
            int yPosition = 0;

            for (int i = 0; i < distance; i++)
            {
                switch (direction)
                {
                    case DiagnalDirection.FORWARD_LEFT:
                        xPosition--;
                        yPosition++;
                        break;
                    case DiagnalDirection.FORWARD_RIGHT:
                        xPosition++;
                        yPosition++;
                        break;
                    case DiagnalDirection.BACKWARD_LEFT:
                        xPosition--;
                        yPosition--;
                        break;
                    case DiagnalDirection.BACKWARD_RIGHT:
                        xPosition++;
                        yPosition--;
                        break;
                    default:
                        break;
                }
                attack[i] = new Point(xPosition, yPosition);
            }
            return attack;
        }
    }
}
