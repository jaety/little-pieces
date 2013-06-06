package jt.littlepieces

object Combine4 {
  sealed class Operator(val f: (Int,Int) => Option[Int])
  case object Plus extends Operator((a,b) => Some(a + b))
  case object Times extends Operator((a,b) => Some(a * b))
  case object RDiv extends Operator((a,b) => if (a != 0 && b % a == 0) Some(b / a) else None)
  case object Div extends Operator((a,b) => if (b != 0 && a % b == 0) Some(a / b) else None)
  case object RMinus extends Operator((a,b) => Some(b - a))
  case object Minus extends Operator((a,b) => Some(a - b))
  val operators = List(Plus, Times, RDiv, Div, RMinus, Minus)

  case class Step(left: Int, right: Int, op: Operator, items: Seq[Int])
  def find(items: Seq[Int], target: Int, result: Seq[Step] = Seq()) : Option[Seq[Step]] = {
    assert(items.length >= 1)
    if (items.length == 1) if (items(0) == target) Some(result) else None
    else {
      def removeAt(s: Seq[Int], inds: Seq[Int]) = s.zipWithIndex.filter(t => !inds.contains(t._2)).map(_._1)
      val t = (0 until items.length).combinations(2).flatMap( inds => {
        val (a,b) = (items(inds(0)), items(inds(1)))
        for (op <- operators;
             next <- op.f(a,b) if (next != 0);
             step = Step(a,b,op,items)) yield find(next +: removeAt(items, inds), target, step +: result)
      })
      t.flatten.toIterable.headOption.map(_.reverse)
    }
  }

  def main(args: Array[String]) {
    println(find(Seq(1,2,4,6), 24))
    println(find(Seq(1,1,1,1), 24))
    println(find(Seq(7,8,8,13), 24))
    println(find(Seq(2,3,12,12),24))
  }
}
