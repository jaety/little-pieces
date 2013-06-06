package jt.littlepieces

import scala.language.implicitConversions
import collection.TraversableLike
import collection.generic.CanBuildFrom

object ChainUtils {
  // This helped me figure it out: http://stackoverflow.com/questions/15709233/pimp-my-library-for-all-traversables
  // TODO: Returning List not Seq. Why?
  implicit class Chainer[T, Repr <: Traversable[T]](val coll: TraversableLike[T, Repr]) extends AnyVal {
    def chain[R1,R2,That](f: TraversableLike[T,Repr] => R1)(f2: (T,R1) => R2)(implicit bf: CanBuildFrom[Repr, R2, That]) : That = {
      val r1 = f(coll)
      coll.map((t:T) => f2(t, r1))
    }
  }

  // TODO: Why doesn't this commented out version work? It compiles, but complains about the call to map
//  implicit class Chainer[T, C[_] <: Traversable[_]](coll: C[T]) {
//      def chain[R1,R2](f: C[T] => R1)(f2: (T,R1) => R2) = {
//      val r1 = f(coll)
//      coll.map((t:T) => f2(t, r1))
//    }
//  }
//  implicit class Chainer[T](coll: Seq[T]) {
//    def chain[R1,R2](f: Seq[T] => R1)(f2: (T,R1) => R2) = {
//      val r1 = f(coll)
//      coll.map((t:T) => f2(t, r1))
//    }
//  }

  implicit class DoubleList(val coll: Seq[Double]) {
//    def normalize(stat: Seq[Double] => Double = _.sum) = coll.chain(stat)(_ / _)
    def normalize = coll.chain(_.sum)(_ / _)
    def normalize(stat: TraversableLike[Double, Seq[Double]] => Double) = coll.chain(stat)(_ / _)
  }
}


object ChainRunner {
  import ChainUtils._
  def main(args: Array[String]) {
    val c = Seq(1.0, 2.0, 3.0, 4.0)
    println(c)
    println(c.chain(_.sum)(_ / _))
    println(c.normalize)
    println(c.normalize(_.min))
    println(c.normalize(s => (s.min + s.max)/2.0))
  }
}