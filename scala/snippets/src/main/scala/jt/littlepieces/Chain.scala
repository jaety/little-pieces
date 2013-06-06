package jt.littlepieces

import scala.language.implicitConversions

object ChainUtils {
// TODO: Why doesn't this commented out version work? It compiles, but complains about the call to map
//  implicit class Chainer[T, C[_] <: Traversable[_]](coll: C[T]) {
//      def chain[R1,R2](f: C[T] => R1)(f2: (T,R1) => R2) = {
//      val r1 = f(coll)
//      coll.map((t:T) => f2(t, r1))
//    }
//  }
  implicit class Chainer[T](coll: Seq[T]) {
    def chain[R1,R2](f: Seq[T] => R1)(f2: (T,R1) => R2) = {
      val r1 = f(coll)
      coll.map((t:T) => f2(t, r1))
    }
  }
}

object ChainRunner {
  import ChainUtils._
  def main(args: Array[String]) {
    val c = Seq(1.0, 2.0, 3.0, 4.0)
    println(new Chainer(c).chain(_.sum)(_ / _))

  }
}