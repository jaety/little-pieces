
trait StateMachine[T, R] {
  protected case class StateResult(value: R, succ: Any)
  protected implicit def toResult(t: (R,Any)) = StateResult(t._1, t._2)

  protected case class State(f: T => StateResult)

  def init: Any
  def states : Map[Any, State]

  trait Iter {
    def apply(v: T) : R
  }
  private class IterImpl extends Iter {
    private var state = init
    def apply(v: T) : R = { val res = states(state).f(v); state = res.succ; res.value }
  }

  def iter : Iter = new IterImpl()

  protected def defineStates(states: (Any,State)*) : Map[Any,State] = states.toMap

}

class MyStateMachine(val init: Any = 0) extends StateMachine[Int, Int] {
  val states = defineStates(
    0 -> State( i => (5, if (i<4) 0 else 1) ),
    1 -> State( i => (10, 1) )
  )
}

object StateMachineRunner extends App {

  val a = Seq(1,2,3,4,5,6,5,4,3,2)
  val sm = new MyStateMachine()
  val smi = sm.iter
  println(a.map(smi(_)))

  val b = Seq(2,1,2,3,5,4,0,1,2,5,4,2).map(_.toDouble)
  val smi2 = new Trends().iter
  println(b.sliding(3).map(smi2(_)).toIndexedSeq)

}
